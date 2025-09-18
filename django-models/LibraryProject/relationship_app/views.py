from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library
class libraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})
# Create your views here.
