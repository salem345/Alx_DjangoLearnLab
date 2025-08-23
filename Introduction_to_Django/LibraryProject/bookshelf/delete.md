# Update operation in Django shell
## Purpose
This document describes the process of deleting a new instance of the 'Book' model using the Django shell.In this example, we will delete the book titled **"1984"** and confirm the deletion by retrieving all 'Book' instances from the database.
'''
import the book model
from bookshelf.models import Book

# Retrieve the book to be deleted
book = Book.objects.get(title = "1984")

book.delete()
# Expected Output: (1,{'library.Book': 1}), indicating one 'Book' instance was deleted

# confirm deletion by retrieving all books

all_books = Book.objects.all()
all_books # Expected Output: <Queryset []> if no other books exist, or a list of remaining books