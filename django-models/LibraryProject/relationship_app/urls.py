from django.urls import path
from . import views
from .views import list_books
urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]