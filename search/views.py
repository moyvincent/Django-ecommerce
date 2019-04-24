from django.shortcuts import render
from products.models import Product
from django.db.models import Q
# Create your views here.


def search_product_list_view(request, *args, **kwargs):
    print(request.GET)
    print(request)
    query = request.GET.get('q', "laptop")
    print(query)
    if query is not None:
        queryset = Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
        lookups = Product.objects.filter(queryset).distinct()
        context = {
            "object_list": lookups
        }
        return render(request, "search_list.html", context)
    else:
        return Product.objects.none()
