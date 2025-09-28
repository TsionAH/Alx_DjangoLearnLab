from rest_framework import serializers
from datetime import datetime
from .models import Book , Author
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id' , 'title' , 'publication_year','author']
    def validate_publication_year(self , value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("publication yera can not be in the future")
        else:
            return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id' , 'name','books']
