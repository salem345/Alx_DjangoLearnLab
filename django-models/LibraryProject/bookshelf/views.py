from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Library
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Bookshelf Home Page")
def book_list(request):
    books = Book.objects.all()
    return HttpResponse(', '.join([book.title for book in books]))

class LibraryListView(ListView):
    model = Library
    template_name = 'bookshelf/library_list.html'
    context_object_name = 'library'



