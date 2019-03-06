from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Author, Quote
from django.contrib.auth.models import User
from taggit.models import Tag
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader

def index(request):
	title = 'Fresh And Latest Quotes'
	quotes = Quote.objects.all().order_by('-date_created')

	page = request.GET.get('page', 1)
	paginator = Paginator(quotes, 20)
	try:
		quotes = paginator.page(page)
	except PageNotAnInteger:
		quotes = paginator.page(1)
	except EmptyPage:
		quotes = paginator.page(paginator.num_pages)	

	context = {
		'title' : title,
		'quotes' : quotes,
	}
	return render(request, 'quote/index.html', context)

def quote(request, id, slug):
	quote = Quote.objects.get(id=id)
	context = {
		'quote' : quote,
	}
	return render(request, 'quote/quote.html', context)

def all_authors(request):
	context = {
		'title' : 'List Of All Authors',
	}
	return render(request, 'quote/all_authors.html', context)

def author(request, slug, id):
	author = Author.objects.get(id=id)
	title = author.name + ' Quotes'
	quotes = author.quotes.all().order_by('-date_created')

	page = request.GET.get('page', 1)
	paginator = Paginator(quotes, 20)
	try:
		quotes = paginator.page(page)
	except PageNotAnInteger:
		quotes = paginator.page(1)
	except EmptyPage:
		quotes = paginator.page(paginator.num_pages)

	context = {
		'author' : author,
		'title' : title,
		'quotes' : quotes,
	}
	return render(request, 'quote/index.html', context)


def tag(request, slug):
	tag = Tag.objects.get(slug=slug)
	title = tag.name + ' Quotes'
	quotes = Quote.objects.filter(tags__name=tag).order_by('-date_created')

	page = request.GET.get('page', 1)
	paginator = Paginator(quotes, 20)
	try:
		quotes = paginator.page(page)
	except PageNotAnInteger:
		quotes = paginator.page(1)
	except EmptyPage:
		quotes = paginator.page(paginator.num_pages)
		
	context = {
		'tag' : tag,
		'title' : title,
		'quotes' : quotes,
	}
	return render(request, 'quote/index.html', context)


@csrf_exempt
def save_quote(request):
	if request.method == 'POST':
		user = request.POST.get('user')
		author = request.POST.get('author')
		quote = request.POST.get('quote')
		tags = request.POST.get('tags')
		bq_url = request.POST.get('bq_url')
		tags = tags.split(',')
		try:
			bq_url = Quote.objects.get(bq_url__iexact=bq_url)
			return HttpResponse('Quote already exists')
		except:
			user = User.objects.get(username__iexact=user)
			try:
				author = Author.objects.get(name__iexact=author)
			except:
				new_author = Author.objects.create(name=author)
				new_author.save()
				author = Author.objects.get(name__iexact=author)

			new_quote = Quote.objects.create(user=user, author=author, quote=quote, bq_url=bq_url)	
			new_quote.save()
			for t in tags:
				new_quote.tags.add(t)
			return HttpResponse('Saved')
		return HttpResponse('Unknown')
	return HttpResponse('Not Allowed')


def search(request):
	if request.method == 'GET':
		term = request.GET.get('term')
		authors = Author.objects.filter(name__icontains=term)
		topics = Tag.objects.filter(name__icontains=term)
		search_html = loader.render_to_string('quote/search.html', {'topics' : topics, 'authors' : authors})
		data = {
			'search_html' : search_html,
		}
		return JsonResponse(data)