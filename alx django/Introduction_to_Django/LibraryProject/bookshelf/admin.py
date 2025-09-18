from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns in admin list view
    search_fields = ('title', 'author')                     # searchable fields
    list_filter = ('publication_year',)                     # filter sidebar

# Register Book with this custom admin
admin.site.register(Book, BookAdmin)
