from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('books/',BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/',BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),

    # JWT Authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
