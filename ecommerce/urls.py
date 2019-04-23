"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, re_path
from ecommerce.views import home_page, about_page, contact_page, login_page, register_page
from products.views import (
    product_list_view,
    product_detail_view,
    product_featured_detail_view,
    product_featured_list_view
)
from search.views import search_product_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('contact', contact_page, name='contact'),
    path('about', about_page, name='about'),
    path('login', login_page, name='login'),
    path('register', register_page, name='register'),
    path('list', product_list_view, name='products'),
    path('search', search_product_list_view, name='search'),
    path('featured', product_featured_list_view),
    re_path(r'^detail/(?P<slug>[\w-]+)/$', product_detail_view),
    re_path(r'^featured/(?P<pk>[\d+])/$', product_featured_detail_view),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
