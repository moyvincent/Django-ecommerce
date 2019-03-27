from django.shortcuts import render

from ecommerce.forms import ContactForm


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