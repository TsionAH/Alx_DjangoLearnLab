from django.urls import path
from .views import ListView, CreateView, DeleteView, DetailView, UpdateView

urlpatterns = [
    path('books/', ListView.as_view(), name='list-books'),
    path('books/<int:pk>/', DeleteView.as_view(), name='delete-book'),
    path('books/create/', CreateView.as_view(), name='create-book'),
    path('books/delete', DetailView.as_view(), name='retrieve-book'),
    path('books/update', UpdateView.as_view(), name='update-book')
]