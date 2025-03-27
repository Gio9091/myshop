
from django.urls import path
from .views import checkout, order_history
app_name = 'orders'
urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('order-history/', order_history, name='order_history'),
]

