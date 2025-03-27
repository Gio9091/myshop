from django.contrib import admin
from django.urls import path, include
from myshop.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cart/", include("cart.urls")),
    path("products/", include(("products.urls", "products"), namespace="products")),
    path("accounts/", include("accounts.urls")),
    path("orders/", include("orders.urls")),
    path("", home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
