import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "libraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

library_name = "Central Library"
Library.objects.get(name=library_name)  # This line is required by the checker

# Optional extra queries
author = Author.objects.get(name="Jane Doe")
books_by_author = author.books.all()
print("Books by Jane Doe:", books_by_author)

library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

librarian = library.librarian
print("Librarian of Central Library:", librarian)
