
# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Registration view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log user in after registration
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')

# Profile view
@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email", request.user.email)
        request.user.save()
    return render(request, "blog/profile.html")
# blog/views.py

def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    # Example context, you can replace with your real data
    context = {
        'posts': []  
    }
    return render(request, 'blog/posts.html', context)