from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'publication_year')
    search_fields = ('author',)
    list_filter = ('author',)


# Register your models here.
admin.site.register(Book, BookAdmin)


