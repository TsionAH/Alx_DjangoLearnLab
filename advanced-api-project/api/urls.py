from django.urls import path
from .views import BookListView, AuthorListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
]
