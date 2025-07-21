from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns in list view
    search_fields = ('title', 'author')                     # enables search bar
    list_filter = ('publication_year',)                     # adds filter sidebar

