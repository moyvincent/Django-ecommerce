from django.shortcuts import render, redirect
from products.models import Product
from carts.models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/home.html', {})

def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.product.all():
        cart_obj.product.remove(product_obj)
    else:
        cart_obj.product.add(product_obj)
    return redirect("cart:home")




