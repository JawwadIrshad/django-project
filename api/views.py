#veiw.py file
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
         return self.queryset.filter(owner=self.request.user)
