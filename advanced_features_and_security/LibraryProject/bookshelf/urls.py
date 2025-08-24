from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("books/search/", views.search_books, name="search_books"),
    path("libraries/<int:pk>/", views.library_detail, name="library_detail"),
    # اختياري:
    path("books/raw/", views.raw_sql_example, name="raw_sql_example"),
]
from django.urls import path
from . import views

urlpatterns = [
    # Existing views
    path("books/", views.book_list, name="book_list"),
    path("books/search/", views.search_books, name="search_books"),
    path("libraries/<int:pk>/", views.library_detail, name="library_detail"),

    # API endpoints
    path("api/books/", views.BookListCreateAPIView.as_view(), name="api_books_list_create"),
    path("api/books/<int:pk>/", views.BookRetrieveUpdateDestroyAPIView.as_view(), name="api_books_detail"),
]