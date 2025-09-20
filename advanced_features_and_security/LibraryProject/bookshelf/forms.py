from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']  # include relevant fields

    # Optional: add custom validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title:  # simple example to prevent XSS
            raise forms.ValidationError("Invalid characters in title")
        return title
