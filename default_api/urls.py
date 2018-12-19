from django.urls import path

from default_api import views

urlpatterns = [
    path('', views.OrderList.as_view()),
    path('<int:pk>/', views.OrderDetail.as_view()),
    path('<int:pk>/lines', views.ItemList.as_view()),
]

