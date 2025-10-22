from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()



    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    def __str__(self):
        return self.name
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# Create your models here.
