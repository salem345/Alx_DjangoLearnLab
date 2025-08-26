from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
# from django_filters import rest_framework

# Create your views here.
class ListView(viewsets.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # filter_backends = [DjangoFilterBackend , filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['title', 'author']
    search_fields = ['title', 'author']
    orderinf_fields = ['title', 'publication_year']
    ordering = ['title']
    
def get_queryset(self):
    queryset = Book.objects.all()
    title = self.request.query_params.get('title')
    if title is not None:
        queryset = queryset.filter(title=title)
    return queryset
    
    
class DetailView(viewsets.RetrieveAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class CreateView(viewsets.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
        
    
    
class UpdateView(viewsets.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['pk'])

class DeleteView(viewsets.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer