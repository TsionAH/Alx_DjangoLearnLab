# relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("register/", views.register_view, name="register"),

    # Use Django's built-in class-based views for auth
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),

    path("books/", list_books, name="list_books"),  # FBV URL
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # CBV URL
]
