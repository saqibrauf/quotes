from django.urls import path, include
from django.contrib.sitemaps import views as sm_views
from .sitemap import AuthorSitemap, QuoteSitemap, TagSitemap
from django.views.generic import TemplateView
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
    path('pages/<slug>/', views.content, name = 'content'), 
    path('quote/<slug>-<id>', views.quote, name = 'quote'),
    path('all-authors', views.all_authors, name = 'all_authors'),
    path('author/<slug>-quotes-<id>', views.author, name = 'author'),
    path('tags/<slug>-quotes', views.tag, name = 'tag'),
    path('search', views.search, name = 'search'),
    path('save-quote', views.save_quote, name = 'save_quote'),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt'), name="robot"),
]