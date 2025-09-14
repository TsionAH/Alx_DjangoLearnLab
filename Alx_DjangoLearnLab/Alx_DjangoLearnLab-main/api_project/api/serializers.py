from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    "Serialzer for the book class"
    class Meta:
        model = Book
        fields = ['title', 'author']