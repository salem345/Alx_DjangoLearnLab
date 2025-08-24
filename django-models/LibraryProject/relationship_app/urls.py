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

from django.urls import path, include

urlpatterns = [
    path('relationship_app/', include('relationship_app.urls')),
]

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Permissions secured views
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]