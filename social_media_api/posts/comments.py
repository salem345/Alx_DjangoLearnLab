from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
permission_classes = [IsAuthenticatedOrReadOnly]
# edit/delete: تحقق من ownership