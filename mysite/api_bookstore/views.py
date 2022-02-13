from django.shortcuts import render
from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

