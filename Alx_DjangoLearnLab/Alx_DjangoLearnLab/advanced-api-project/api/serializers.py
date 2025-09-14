from datetime import datetime
from rest_framework import serializers
from models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    """Serialzer for the book model."""
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    """
        Validates the publication year. Ensures the publication year of a book
        is not set in the future
    """
    def validate_publication_year(self, value):
        if value > datetime.today().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value
    
    def validate(self, data):
        """
        Validates the title and author.
        """
        if not data.get('title'):
            raise serializers.ValidationError({"title": "title must contain at least one character"})
        
        if not data.get('author'):
            raise serializers.ValidationError({"author": "author must contain at least one character"})
        
        return data


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. Each Author has book objects displayed under them
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']


