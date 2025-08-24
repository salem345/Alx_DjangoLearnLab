from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("books/search/", views.search_books, name="search_books"),
    path("libraries/<int:pk>/", views.library_detail, name="library_detail"),
    # اختياري:
    path("books/raw/", views.raw_sql_example, name="raw_sql_example"),
]