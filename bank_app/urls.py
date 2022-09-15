from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer),
    path('create/', views.create_customer),
    path('update/<int:id>', views.update_customer),
    path('delete/<int:id>', views.delete_customer)
]