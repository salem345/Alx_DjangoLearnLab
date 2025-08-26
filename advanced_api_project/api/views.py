from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

# ✅ نكتب Permission مخصصة
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # السماح بالقراءة للجميع (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # الكتابة، التعديل، الحذف → للمشرفين فقط (is_staff)
        return request.user and request.user.is_staff


# ✅ List all books OR create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]  # نستخدم الـ Permission الجديد

    # ✅ فلترة وبحث وترتيب
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year']


# ✅ Retrieve, Update, or Delete a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]