from django.urls import path
from .views import AuthorCreateView, AuthorUpdateView, BookCreateView, BookDeleteView, BookListView, BookUpdateView, PublisherListView, AuthorListView, get_searched_books

urlpatterns = [

    path('', BookListView.as_view(), name = 'books'),
    path('search', BookListView.as_view(), name = 'search'),
    path('ajax-search/', get_searched_books, name='ajax-search'),
    

    path('edit-book/<int:id>/', BookUpdateView.as_view()),
    path('delete-book/<int:id>/', BookDeleteView.as_view()),
    path('edit-book/', BookCreateView.as_view(), name='add'),

    path('publishers/', PublisherListView.as_view(), name="publishers"),
    path('authors/', AuthorListView.as_view(), name="authors"),
    path('books/<title>/', BookListView.as_view(), name="books"),
    path('authors/create', AuthorCreateView.as_view()),
    path('authors/update/<pk>/', AuthorUpdateView.as_view()),
    
    
    # path('', index),
    # path('contacts/', contacts),
    # path('regions/', get_regions),
    # path('regions/edit/', edit_region),
    # path('regions/<int:id>', get_regions),
    # path('regions/<slug:text>', find_by_name),
    # re_path('regions/$', find_by_name),
]
