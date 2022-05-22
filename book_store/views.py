from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.core import serializers

from book_store.models import Author, Book, Publisher

# Create your views here.


class PublisherListView(ListView):
    model = Publisher
    template_name = 'publishers.html'
    context_object_name = 'my_favorite_publishers'


class AuthorListView(ListView):
    #queryset = Author.objects.all()
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'


class PublisherDetailView(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


class BookListView(ListView):
    model = Book
    template_name = 'index.html'
    # context_object_name = 'books'
    # queryset = Book.objects.filter(title__icontains = 'j')

    def get_context_data(self, **kwargs):
        q = Book.objects.all()

        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(title__icontains=text) | Q(authors__name__icontains=text) | Q(description__icontains=text))
        
        if 'from-price' in url_dict and url_dict['from-price']:
            from_price = int(url_dict['from-price'])
            q = q.filter(price__gte=from_price)
        
        if 'to-price' in url_dict and url_dict['to-price']:
            to_price = int(url_dict['to-price'])
            q = q.filter(price__lte=to_price)

        context = {'books': q}
        return context


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name']
    template_name = 'create-author.html'


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']
    template_name = 'update-author.html'

    def get_object(self):
        print(self.request.GET.get('pk'))
        return Author.objects.get(pk=1)


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'authors', 'description',
              'price', 'publisher', 'publication_date', 'image']
    template_name = 'edit-book.html'
    context_object_name = 'form'
    success_url = '/book-store'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'authors', 'description',
              'price', 'publisher', 'publication_date', 'image']
    template_name = 'edit-book.html'
    context_object_name = 'form'
    success_url = '/'

    def get_object(self):
        return Book.objects.get(pk=self.kwargs.get('id'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.object.id
        return context


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/book-store'
    template_name = 'book-delete-conf.html'

    def get_object(self):
        return Book.objects.get(pk=self.kwargs.get('id'))

def get_searched_books(request):
    print(request.GET)
    q = Book.objects.all()

    url_dict = request.GET
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

    serialized_queryset = serializers.serialize('python', q)
    return JsonResponse(serialized_queryset, safe=False)
