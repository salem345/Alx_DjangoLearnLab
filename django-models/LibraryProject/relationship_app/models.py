from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)    
    def __str__(self):
        return self.name

class Book(models.Model):
     title = models.CharField(max_length=255)
     author = models.ForeignKey('Author', on_delete=models.CASCADE)
     publication_year = models.IntegerField(null=True, blank=True)

     def __str__(self):
        return self.title

     class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]
class Library(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
class login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class logout(models.Model):
    username = models.CharField(max_length=150)

    def __str__(self):
        return self.username

class register(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    choices = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    ]
    role = models.CharField(max_length=20, choices=choices, default='member')

    def __str__(self):
        return f"{self.user.username}'s profile"