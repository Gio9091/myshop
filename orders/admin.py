from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at')
    search_fields = ('user__username',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
