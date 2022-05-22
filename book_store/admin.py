from atexit import register
from django.contrib import admin

from book_store.models import Author, Book, Publisher

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)