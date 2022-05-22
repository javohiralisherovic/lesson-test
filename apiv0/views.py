from django.shortcuts import render
from rest_framework import viewsets
from book_store.models import *
from .serializer import *
from django.db.models import Q
from rest_framework import permissions
from rest_framework import generics

# Create your views here.
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    #queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = Book.objects.all()
        url_dict = self.request.GET
        print(url_dict)
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(title__icontains=text) | Q(
                authors__name__icontains=text) | Q(description__icontains=text))

        if 'from-price' in url_dict and url_dict['from-price']:
            from_price = int(url_dict['from-price'])
            q = q.filter(price__gte=from_price)

        if 'to-price' in url_dict and url_dict['to-price']:
            to_price = int(url_dict['to-price'])
            q = q.filter(price__lte=to_price)

        return q


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer

    def get_object(self):
        return Book.objects.get(pk=self.request.data.get('id'))

class BookUpdateView(generics.UpdateAPIView):

    serializer_class = BookSerializer
    def get_object(self):
        return Book.objects.get(pk=self.request.data.get('id'))


class BookDestroyView(generics.DestroyAPIView):

    serializer_class = BookSerializer

    def get_object(self):
        return Book.objects.get(pk=self.request.data.get('id'))
