from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import CartItem
from .models import Order, OrderItem
from django.urls import reverse

def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})

def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items:
        messages.error(request, "თქვენი კალათა ცარიელია!")
        return redirect('cart:cart_detail')

    total_price = sum(item.quantity * item.product.price for item in cart_items)


    order = Order.objects.create(user=request.user, total_price=total_price)


    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )


    cart_items.delete()

    messages.success(request, "შეკვეთა წარმატებით გაიგზავნა!")
    return redirect(reverse('orders:order_history'))
