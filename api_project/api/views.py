from rest_framework import generics, viewsets,permissions
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly


# Existing ListAPIView (still works)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔒 require login
    permission_classess = [IsAuthorOrReadOnly]
