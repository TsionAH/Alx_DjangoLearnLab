
# CRUD operations

## CREATE

>>> from bookshelf.models import Book
>>> book_2 = Book(title = "1984", author = "George Orwell", publication_year = "1949")
>>> book_2.save()

### Expected Output

>>>

## Retrieve

>>> print(vars(book_1))

### Expected output

{'_state': <django.db.models.base.ModelState object at 0x10352ae90>, 'id': 2, 'title': '1984', 'author': 'George Orwell', 'publication_year': '1949'}

### Output

>>> print(vars(book_2))

{'_state': <django.db.models.base.ModelState object at 0x10352ae90>, 'id': 2, 'title': '1984', 'author': 'George Orwell', 'publication_year': '1949'}
>>>

## Update

>>> book_2.title = "Nineteen Eighty-Four"

### Expected Output

'Nineteen Eighty-Four'

### Output (new title)

>>> book_2.title
'Nineteen Eighty-Four'

## Delete

>>> book_2.delete()
(1, {'bookshelf.Book': 1})

### Expected Output

>>> Book.objects.all()
<QuerySet []>

### Output (delete)

>>> Book.objects.all()
<QuerySet []>
