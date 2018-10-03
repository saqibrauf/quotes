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
    path('quote/<slug>', views.quote, name = 'quote'),
    path('quotes-of-<slug>', views.author, name = 'author'),
    path('<slug>-quotes', views.tag, name = 'tag'),
]