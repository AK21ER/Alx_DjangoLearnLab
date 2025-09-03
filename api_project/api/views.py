from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView (still works)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
