from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("add/", views.add_product, name="add_product"),
    path("", views.product_list, name="product_list"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
]
