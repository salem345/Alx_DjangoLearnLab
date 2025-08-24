# Update operation in Django shell
## Purpose
'''
from bookshelf.models import Book

# Retrieve the book by title
book = Books.object.get(title = "1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save() # save the changes to database
# Expected output: 'Nineteen Eighty-Four', confirming the title has been updated
book.title # Output: 'Nineteen Eighty-Four'
'''