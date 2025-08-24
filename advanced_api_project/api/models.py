from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """
    Model representing an author.
    Fields:
        - name: stores the author's name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    Fields:
        - title: the book's title.
        - publication_year: the year the book was published.
        - author: ForeignKey linking to Author (one-to-many relationship).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    search_fields = ['title', 'author']
    ordering = ['title', 'publication_year']
    
    def __str__(self):
        return self.title

# Create your models here.
