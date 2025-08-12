from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

# ------------------------
# AUTHENTICATION VIEWS
# ------------------------

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('list_books')  # Update this if needed
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('list_books')  # Update this if needed
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return render(request, 'relationship_app/logout.html')


# ------------------------
# ROLE-BASED VIEWS
# ------------------------

def check_role(role):
    def inner(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return inner


@login_required
@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


    

@login_required
@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    pass  # placeholder until implemented

def add_book(request):
    # your view logic here
    return render(request, 'add_book.html')


@login_required
def edit_book(request, book_id):
    # book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # handle edit logic here
        return HttpResponse(f"Book {book_id} edited (stub)")
    return render(request, 'edit_book.html', {'book_id': book_id})

@login_required
def delete_book(request, book_id):
    # book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # handle delete logic here
        return HttpResponse(f"Book {book_id} deleted (stub)")
    return render(request, 'delete_book.html', {'book_id': book_id})

@login_required
def admin_view(request):
    return HttpResponse("Admin view (stub)")

@login_required
def librarian_view(request):
    return HttpResponse("Librarian view (stub)")

@login_required
def member_view(request):
    return HttpResponse("Member view (stub)")