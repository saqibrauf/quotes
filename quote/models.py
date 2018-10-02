from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import datetime
from taggit.managers import TaggableManager


class Author(models.Model):
	author_name = models.CharField(max_length=100, unique=True)
	author_slug = models.SlugField(max_length=100, editable=False)

	def __str__(self):
		return self.author_name.title()

	def save(self, *args, **kwargs):
		self.author_slug = slugify(self.author_name)
		super().save(*args, **kwargs)
	
	def get_absolute_url(self):
		return reverse('author', args=[str(self.author_slug)])


class Quote(models.Model):
	#user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	author_name = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
	date_created = models.DateTimeField(auto_now=True)
	quote = models.TextField(unique=True)
	tags = tags = TaggableManager()
	quote_slug = models.SlugField(max_length=100, blank=True, editable=False)

	def __str__(self):
		return Truncator(self.quote).chars(100, truncate='') + ' (' + self.author_name.author_name.title() + ')'

	def save(self, *args, **kwargs):
		self.quote_slug = Truncator(slugify(self.quote)).chars(100, truncate='')
		if not self.author_name:
			author = Author.objects.get(author_name='Anonymous')
			self.author_name = author
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('quote', args=[str(self.quote_slug)])

