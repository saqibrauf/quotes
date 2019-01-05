from django.urls import path, include
from django.contrib.sitemaps import views as sm_views
from .sitemap import AuthorSitemap, QuoteSitemap, TagSitemap
from . import views

sitemaps = {
    'author' : AuthorSitemap(),
    'quote' : QuoteSitemap(),
    'tag' : TagSitemap(),
}

urlpatterns = [
	#Sitemap
	path('sitemap.xml/', sm_views.index, {'sitemaps' : sitemaps }, name='django.contrib.sitemaps.views.sitemap'),
	path('sitemap-<section>.xml/', sm_views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),


    path('', views.index, name = 'index'),
    path('quote/<slug>-<id>', views.quote, name = 'quote'),
    path('author/<slug>-quotes-<id>', views.author, name = 'author'),
    path('tags/<slug>-quotes', views.tag, name = 'tag'),
    path('save-quote', views.save_quote, name = 'save_quote'),
]