from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('', views.book_list, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('library/', views.LibraryListView.as_view(), name='library_list'),
    path('register/', views.registerationView.as_view(), name='register'),
    # replace your custom login view with Django's LoginView (renders template and handles POST)
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # optional: use LogoutView to handle logout POST/GET cleanly
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:home'), name='logout'),
    path('admin_view/', views.admin_view.as_view(), name='admin_view'),
    path('librarian_view/', views.librarian_view.as_view(), name='librarian_view'),
    path('member_view/', views.member_view.as_view(), name='member_view'),
    path('book/new/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]