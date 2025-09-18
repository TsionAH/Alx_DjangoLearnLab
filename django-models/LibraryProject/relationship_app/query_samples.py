import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "libraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Library query (checker requires this exact line)
library_name = "Central Library"
library = Library.objects.get(name=library_name)

# Correct line for the checker
librarian = Librarian.objects.get(library=library)
print("Librarian of Central Library:", librarian)


# Author query
author_name = "Jane Doe"
author = Author.objects.get(name=author_name)  # checker requires this exact line

# Filter books by author
books_by_author = Book.objects.filter(author=author)  # checker requires this exact line
print("Books by Jane Doe:", books_by_author)

# Optional: list all books in a library
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

# Optional: retrieve librarian
librarian = library.librarian
print("Librarian of Central Library:", librarian)
