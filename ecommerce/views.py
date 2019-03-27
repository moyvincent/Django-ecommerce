from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from ecommerce.forms import ContactForm, LoginForm, RegisterForm


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


def login_page(request):
    form = LoginForm(request.POST or None)  # assigns the data in LoginForm to the form variable
    context = {
        "title": "Enter Details",
        "login": form
    }
    if form.is_valid():  # checks if form is valid
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            login(request, user)
            return redirect("/") #redirects back to the login page
        else:
            print("error")
    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "title": "Sign up with us",
        "register": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)