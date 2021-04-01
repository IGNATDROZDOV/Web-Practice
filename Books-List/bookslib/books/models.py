from django.db import models
from django.shortcuts import reverse

class Book(models.Model):
	slug = models.SlugField(max_length=100, unique=True)
	title = models.CharField(max_length=200,db_index=True)
	upl_date = models.DateField(auto_now_add=True)
	body = models.FileField(upload_to='media')
	authors = models.ManyToManyField('Author', related_name='books')
	short_desc = models.CharField(max_length=200, blank=True)

	def get_absolute_url(self):
		return reverse('get_book_detail_url', kwargs={'slug':self.slug})

	def __str__(self):
		return self.title


class Author(models.Model):
	slug = models.SlugField(max_length=100, unique=True)
	name = models.CharField(max_length=100, db_index=True)
	surname = models.CharField(max_length=100, db_index=True)

	def get_absolute_url(self):
		return reverse('get_author_detail_url', kwargs={'slug':self.slug})

	def __str__(self):
		return f'{self.name} {self.surname}'