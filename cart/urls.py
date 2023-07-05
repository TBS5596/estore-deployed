from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/<int:pk>', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('add/<int:pk>', views.add_to_orders, name='add_to_orders'),
    path('orders', views.orders, name='orders')
]