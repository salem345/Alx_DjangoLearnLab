from django.contrib import admin
from .models import Book, Library, Author, Librarian


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']

class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ['name', 'library']




# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Library,LibraryAdmin)
admin.site.register(Librarian,LibrarianAdmin)