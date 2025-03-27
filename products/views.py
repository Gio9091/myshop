from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product, Category


def product_list(request):
    category_slug = request.GET.get('category', None)
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    return render(request, "products/product_list.html", {
        "products": products,
        "categories": categories,
        "selected_category": category_slug
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("home")
    else:
        form = ProductForm()
    return render(request, "products/add_product.html", {"form": form})
