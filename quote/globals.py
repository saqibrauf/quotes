from .models import Author, Quote, Content
from taggit.models import Tag
from django.db.models import Count


def global_vars(request):
	CONTENT = Content.objects.all()
	AUTHORS = Author.objects.all().order_by('name')
	SIDEBAR_AUTHORS = Author.objects.annotate(num_quotes=Count('quotes')).order_by('-num_quotes')
	SIDEBAR_TOPICS = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')
	
	return {
		'CONTENT' : CONTENT,
		'AUTHORS' : AUTHORS,
		'SIDEBAR_AUTHORS' : SIDEBAR_AUTHORS,
		'SIDEBAR_TOPICS' : SIDEBAR_TOPICS,
	}