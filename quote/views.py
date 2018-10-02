from django.shortcuts import render
from .models import Author, Quote
from taggit.models import Tag

def index(request):
	quotes = Quote.objects.all().order_by('date_created')
	author_list = Author.objects.all().order_by('author_name')
	tag_cloud = Tag.objects.all()
	context = {
		'quotes' : quotes,
		'author_list' : author_list,
		'tag_cloud' : tag_cloud,
	}
	return render(request, 'quote/index.html', context)

def quote(request, slug):
	quote = Quote.objects.get(quote_slug=slug)
	author_list = Author.objects.all().order_by('author_name')
	tag_cloud = Tag.objects.all()
	context = {
		'quote' : quote,
		'author_list' : author_list,
		'tag_cloud' : tag_cloud,
	}
	return render(request, 'quote/quote.html', context)

def author(request, slug):
	author = Author.objects.get(author_slug=slug)
	quotes = author.quote_set.all()
	author_list = Author.objects.all().order_by('author_name')
	tag_cloud = Tag.objects.all()
	context = {
		'author' : author,
		'quotes' : quotes,
		'tag_cloud' : tag_cloud,
		'author_list' : author_list,
	}
	return render(request, 'quote/author.html', context)


def tag(request, slug):
	tag = Tag.objects.get(slug=slug)
	quotes = Quote.objects.filter(tags__name__in=[tag.name])
	tag_cloud = Tag.objects.all()
	author_list = Author.objects.all().order_by('author_name')
	context = {
		'tag' : tag,
		'quotes' : quotes,
		'tag_cloud' : tag_cloud,
		'author_list' : author_list,
	}
	return render(request, 'quote/tag.html', context)