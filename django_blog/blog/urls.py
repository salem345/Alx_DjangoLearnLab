from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
                    CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts)
#I'm here
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView, name='create-comment'),
    path('comment/<int:pk>/update/', views.CommentUpdateView, name='update-comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView, name='delete-comment'),
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', views.TaggedPostListView.as_view(), name='tagged-posts'),
    path('tags/<slug:tag_slug>/posts/', views.PostByTagListView.as_view(), name='posts-by-tag'),

]