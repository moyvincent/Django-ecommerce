from django.shortcuts import render


def home_page(request):
    context = {
        "title": "Welcome to our Home Page"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "Welcome to our About Page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {
        "title": "Contact Us"
    }
    return render(request, "contact_page.html", context)