from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class CommonInfo(models.Model):
    created_by_user = models.ForeignKey(get_user_model(), related_name='%(app_label)s_%(class)s_created',
                                        on_delete=models.PROTECT, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by_user = models.ForeignKey(get_user_model(), related_name='%(app_label)s_%(class)s_modified',
                                         on_delete=models.PROTECT, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    seq_id = models.PositiveIntegerField(default=1)
    is_system = models.BooleanField(default=0, help_text="System required fields")
    is_active = models.BooleanField(default=1, help_text="Allows a record to be toggled inactive")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if hasattr(self, 'seq_id'):
            self.seq_id = self.seq_id + 1
        else:
            self.seq_id = 1
        super().save(*args, **kwargs)


class Order(CommonInfo):
    number = models.PositiveIntegerField()
    description = models.CharField(max_length=255)


class Line(CommonInfo):
    UOM_CHOICES = (
        ('ea', 'Each'),
        ('ft', 'Feet'),
        ('yd', 'Yards'),
    )
    sku = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=200, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    uom = models.CharField(max_length=2, choices=UOM_CHOICES, default='ea')
    is_taxable = models.BooleanField(default=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lines')

    def sub_total(self):
        return self.price * self.quantity
