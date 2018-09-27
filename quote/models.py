from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import datetime


class Author(models.Model):
	author_name = models.CharField(max_length=100)
	author_slug = models.SlugField(max_length=100, editable=False)

	def __str__(self):
		return self.author_name.title()

	def save(self, *args, **kwargs):
		self.author_slug = slugify(self.author_name)
		super().save(*args, **kwargs)
	"""
	def get_absolute_url(self):
		return reverse('author', args=[str(self.author_slug)])
	"""

class Tag(models.Model):
	tag_name = models.CharField(max_length=50)
	tag_slug = models.SlugField(max_length=50, editable=False)

	def __str__(self):
		return self.tag_name.upper()

	def save(self, *args, **kwargs):
		self.tag_slug = slugify(self.tag_name)
		super().save(*args, **kwargs)


class Quote(models.Model):
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now=True)
	quote = models.TextField()
	tags = models.ManyToManyField(Tag, blank=True)
	quote_slug = models.SlugField(max_length=100, blank=True, editable=False)

	def __str__(self):
		return Truncator(self.quote).chars(100, truncate='') + ' (' + self.author_name.author_name.title() + ')'

	def save(self, *args, **kwargs):
		self.quote_slug = Truncator(slugify(self.quote)).chars(100, truncate='')
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('quote', args=[str(self.quote_slug)])

