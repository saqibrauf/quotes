from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Quote
from django.contrib.auth.models import User
from taggit.models import Tag
from django.views.decorators.csrf import csrf_exempt

def index(request):
	title = 'Recent Quotes'
	quotes = Quote.objects.all().order_by('date_created')
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

def author(request, slug, id):
	author = Author.objects.get(id=id)
	title = author.name + ' Quotes'
	quotes = author.quotes.all()
	context = {
		'title' : title,
		'quotes' : quotes,
	}
	return render(request, 'quote/index.html', context)


def tag(request, slug):
	tag = Tag.objects.get(slug=slug)
	title = tag.name + ' Quotes'
	quotes = Quote.objects.filter(tags__name=tag)
	context = {
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