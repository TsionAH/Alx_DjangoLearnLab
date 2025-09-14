from django.shortcuts import render, redirect
from models import CustomUser, Book
from .forms import ExampleForm
from django.contrib.auth.decorators import permission_required


# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def view_user(request):
    pass

@permission_required('bookshelf.can_create', raise_exception=True)
def create_user(request):
    if request.method == 'POST':
        # Create a form instance from the POST data
        form = ExampleForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the new user object
            user = form.save()
            
            # Redirect to a success URL after saving
            return redirect('some_success_url')
    else:
        # If it's a GET request, create an empty form
        form = ExampleForm()

    # Render the template with the form
    return render(request, 'bookshelf/form_example.html', {'form': form})



@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request):
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_user(request):
    pass


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):

    book_list = Book.objects.all()

    context = {'book_list':  book_list }

    return render(request, 'bookshelf/templates/list_books.html', context)
    
