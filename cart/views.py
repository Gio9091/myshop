from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.models import Product
from .models import CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} დაემატა კალათაში!")
    return redirect('cart:cart_detail')


def cart_detail(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.quantity * item.product.price for item in items)

    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})


def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    cart_item.delete()

    messages.success(request, "პროდუქტი წაიშალა კალათიდან!")
    return redirect('cart:cart_detail')
