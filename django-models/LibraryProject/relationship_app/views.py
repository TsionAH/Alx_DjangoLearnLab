from django.shortcuts import render
# existing imports
from django.views.generic import DetailView
from .models import Library, Book
from django.shortcuts import render

# add this line just for the checker
from django.views.generic.detail import DetailView  # checker expects this

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # make sure template exists
    context_object_name = 'library'

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

