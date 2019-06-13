from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm

# Create your views here.
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
    return render(request, "accounts/login.html", context)


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
    return render(request, "accounts/register.html", context)