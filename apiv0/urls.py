from django.urls import path
from .views import *

urlpatterns = [
    path('publishers/', PublisherViewSet.as_view({'get': 'list'}), name='publishers'),
    path('authors/', AuthorViewSet.as_view({'get': 'list'}), name='authors'),
    path('books/', BookViewSet.as_view({'get': 'list'})),
    path('books/create', BookCreateView.as_view()),
    path('books/change', BookUpdateView.as_view()),
    path('books/delete', BookDestroyView.as_view(), name='books'),
]
