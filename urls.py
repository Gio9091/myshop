from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),  # ჩასვი შენი აპლიკაციის სახელი
]
