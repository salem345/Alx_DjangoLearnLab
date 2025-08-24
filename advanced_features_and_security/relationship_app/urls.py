from django.urls import path
from .import views
from .views import list_books
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]


views.register
from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    views.login_view.as_view(template_name="relationship_app/login.html"),
    views.register_view.as_view(template_name="relationship_app/register.html"),
    views.logout_view.as_view(template_name="relationship_app/logout.html"),
    path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('register/', views.register_view, name='register'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Book permissions secured views
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
]