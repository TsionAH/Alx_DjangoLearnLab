from models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Frank Herbert"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# List all books in a library.
library_name = "Sea Point Library" 
library = Library.objects.get(name=library_name)
all_books = library.books.all()

# Retrieve the librarian for a library.
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
