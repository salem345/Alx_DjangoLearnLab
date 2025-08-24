from django.urls import path
from .import views
from .views import list_books
urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]


views.register
from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    views.LoginView.as_view(template_name="relationship_app/login.html"),
    views.RegisterView.as_view(template_name="relationship_app/register.html"),
    views.LogoutView.as_view(template_name="relationship_app/logout.html"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]