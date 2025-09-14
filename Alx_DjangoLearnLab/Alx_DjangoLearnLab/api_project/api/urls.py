
from django.contrib import admin
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework import routers
from rest_framework.authtoken import views


router = routers.DefaultRouter()

router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('book/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    
]