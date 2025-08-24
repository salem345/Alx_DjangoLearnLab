from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="books-list"),
    path("books/add/", views.add_book, name="books-add"),
    path("books/<int:pk>/edit/", views.edit_book, name="books-edit"),
    path("books/<int:pk>/delete/", views.delete_book, name="books-delete"),
]