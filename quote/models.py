from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import datetime
from taggit.managers import TaggableManager


class Content(models.Model):
	title = models.CharField(max_length=255, unique=True)
	content = models.TextField(blank=True)
	slug = models.SlugField(blank=True, editable=False)

	def __str__(self):
		return self.title.title()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)
	
	def get_absolute_url(self):
		return reverse()

class Author(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, editable=False)

	def first_letter(self):
		return self.name and self.name[0] or ''

	def __str__(self):
		return self.name.title()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
	
	def get_absolute_url(self):
		return reverse('author', args=[str(self.slug), str(self.id)])


class Quote(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes')
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
	date_created = models.DateTimeField(auto_now=True)
	quote = models.TextField()
	tags = TaggableManager(blank=True)
	slug = models.SlugField(max_length=200, blank=True, editable=False)
	bq_url = models.CharField(max_length=250, blank=True, null=True, verbose_name='BQ URL', editable=False)

	def __str__(self):
		return self.quote[:50] + ' (' + self.author.name.title() + ')'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.quote[:100])
		if not self.user:
			self.user = User.objects.get(username='amadarsal')
		if not self.author:
			author = Author.objects.get(name='Anonymous')
			self.author = author
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['-date_created']

	def get_absolute_url(self):
		return reverse('quote', args=[str(self.slug), str(self.id)])

