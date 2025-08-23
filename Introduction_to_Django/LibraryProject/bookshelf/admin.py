from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

    admin.site.register(Book,)

    def __str__(self):
        return self.title

# Register your models here.
