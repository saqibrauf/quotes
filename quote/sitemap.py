from django.contrib.sitemaps import Sitemap
from .models import Author, Quote
from taggit.models import Tag

class AuthorSitemap(Sitemap):    
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Author.objects.all()

class QuoteSitemap(Sitemap):    
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Quote.objects.all()

class TagSitemap(Sitemap):    
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Tag.objects.all()