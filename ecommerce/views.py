from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from ecommerce.forms import ContactForm


def home_page(request):
    context = {
        "title": "Welcome to our Home Page"
    }
    if request.user.is_authenticated:
        context["Auth"] = "I have got privileges"

    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "Welcome to our About Page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Us",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact_page.html", context)