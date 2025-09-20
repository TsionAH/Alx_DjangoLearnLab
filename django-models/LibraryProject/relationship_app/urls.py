from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
     path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('books/', list_books, name='list_books'),  # FBV URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV URL
]
