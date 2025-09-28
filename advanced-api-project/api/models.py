from django.db import models
from rest_framework import generics
from .serializers import BookSerializer
from.serializers import AuthorSerializer
class Author(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
