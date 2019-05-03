from django.contrib.sitemaps import Sitemap
from .models import Author, Quote
from taggit.models import Tag
from django.urls import reverse

class AuthorSitemap(Sitemap):    
    changefreq = "daily"
    priority = 1.0
    limit = 2000

    def items(self):
        return Author.objects.all()

class QuoteSitemap(Sitemap):    
    changefreq = "daily"
    priority = 1.0
    limit = 2000

    def items(self):
        return Quote.objects.all()

class TagSitemap(Sitemap):    
    changefreq = "daily"
    priority = 1.0
    limit = 2000

    def items(self):
        return Tag.objects.all()

    def location(self, item):
    	return reverse('tag', args=[str(item.slug)])