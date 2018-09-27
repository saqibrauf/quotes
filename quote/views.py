from django.shortcuts import render
from .models import Author, Quote, Tag

def index(request):
	quotes = Quote.objects.all().order_by('date_created')
	tag_cloud = Tag.objects.all()
	context = {
		'quotes' : quotes,
		'tag_cloud' : tag_cloud,
	}
	return render(request, 'quote/index.html', context)

def quote(request, slug):
	quote = Quote.objects.get(quote_slug=slug)
	tag_cloud = Tag.objects.all()
	context = {
		'quote' : quote,
		'tag_cloud' : tag_cloud,
	}
	return render(request, 'quote/quote.html', context)

def author(request, slug):
	author = Author.objects.get(author_slug=slug)
	quotes = author.quote_set.all()
	tag_cloud = Tag.objects.all()
	context = {
		'author' : author,
		'quotes' : quotes,
		'tag_cloud' : tag_cloud,
	}
	return render(request, 'quote/author.html', context)

def tag(request, slug):
	tag = Tag.objects.get(tag_slug=slug)
	quotes = tag.quote_set.all()
	tag_cloud = Tag.objects.all()
	context = {
		'tag' : tag,
		'quotes' : quotes,
		'tag_cloud' : tag_cloud,
	}
	return render(request, 'quote/tag.html', context)