from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    # Get author by name
    author = Author.objects.get(name=author_name)
    # Get all books written by this author
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    # Get the library
    library = Library.objects.get(name=library_name)
    # Get all books in this library
    books = library.books.all()
    return books

def get_librarian_for_library(library_name):
    # Get the library
    library = Library.objects.get(name=library_name)
    # Retrieve the librarian (OneToOne relationship)
    librarian = library.librarian
    return librarian