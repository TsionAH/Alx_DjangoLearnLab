from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'publication_year')
    search_fields = ('author',)
    list_filter = ('author',)

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'date_of_birth', 'image')
    search_fields = ('username', 'email', 'first_name' )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)



