# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test

from .models import Book, Library


# ------------------------------
# Library Views
# ------------------------------

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


def list_books(request):
    books = Book.objects.all()  # Get all books
    return render(request, 'list_books.html', {'books': books})


# ------------------------------
# Auth Views (Register, Login, Logout)
# ------------------------------

# Registration view (using UserCreationForm)
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # <-- built-in form
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user after registering
            return redirect("home")  # redirect to homepage
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# Logout view
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# ------------------------------
# Role-based Views
# ------------------------------

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
