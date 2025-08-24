from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import CustomUser ,  CustomUserAdmin

admin.site.register(CustomUser, CustomUserAdmin)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

# Register your models here.
