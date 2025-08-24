from django.urls import path, include
from .views import BookList, BookViewSet
from .router import router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
