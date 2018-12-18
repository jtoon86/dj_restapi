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
