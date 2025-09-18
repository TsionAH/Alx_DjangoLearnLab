from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # add app folder prefix
    context_object_name = 'library'

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

