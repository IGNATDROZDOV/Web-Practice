from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all/', BooksList.as_view(), name='get_books_url'),
    path('book/<str:slug>', BookDetail.as_view(), name='get_book_detail_url'),
    path('author/<str:slug>', AuthorDetail.as_view(), name='get_author_detail_url'),
    path('authors/', AuthorList.as_view(), name='get_authors_url'),
]

