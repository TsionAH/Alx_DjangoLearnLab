
# CRUD operations

## Delete

>>> from bookshelf.models import Book
>>> book.delete()
(1, {'bookshelf.Book': 1})

### Expected Output

>>> Book.objects.all()
<QuerySet []>

### Output

>>> Book.objects.all()
<QuerySet []>
