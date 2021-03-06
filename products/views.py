from django.http import Http404
from django.shortcuts import render, get_object_or_404
from products.models import Product
from carts.models import Cart
# Create your views here.


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_detail_view(request, slug, *args, **kwargs):
    # instance = get_object_or_404(Product, slug=slug)
    qs = Product.objects.filter(slug=slug)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
        cart_obj, new_obj = Cart.objects.new_or_get(request)
    else:
        raise Http404("Product not found")
    context = {
        "object": instance,
        "cart": cart_obj
    }
    return render(request, "products/product_detail.html", context)

""" def get_context_data(self, *args, **kwargs):
    context = super(product_detail_view, self).get_context_data(*args, **kwargs)
    cart_obj, new_obj = Cart.objects.new_or_get(self.request)
    context['cart'] = cart_obj
    print(context)
    return context """


def product_featured_detail_view(request, pk=None, *args, **kwargs):
    instance = get_object_or_404(Product, pk=pk, featured=True)
    if instance is None:
        raise Http404("Not featured")
    context = {
        "object": instance
    }
    return render(request, "products/product_featured_detail.html", context)


def product_featured_list_view(request, *args, **kwargs,):
    queryset = Product.objects.filter(*args, **kwargs, featured=True)
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_featured_list.html", context)