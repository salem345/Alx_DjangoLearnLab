from django.urls import path, include
from .views import BookList, BookViewSet
from .routers import router

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
