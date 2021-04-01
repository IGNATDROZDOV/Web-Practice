from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse


class BooksList(View):
	def get(self, request):
		query_sr = request.GET.get('search', '')
		if query_sr:
			books = Book.objects.filter(title__icontains=query_sr)
		else:
			books = Book.objects.all()
		return render(request, 'books/list_of_books.html', context={'books':books})


class BookDetail(View):
	def get(self, request, slug):
		book = Book.objects.get(slug__iexact=slug)
		return render(request, 'books/book_detail.html', context={'book':book})


class AuthorList(View):
	def get(self, request):
		authors = Author.objects.all()
		return render(request, 'books/authors.html', context={'authors':authors})


class AuthorDetail(View):
	def get(self, request, slug):
		author = Author.objects.get(slug__iexact=slug)
		return render(request, 'books/author_detail.html', context={'author':author})


def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/body")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response
	raise Http404	