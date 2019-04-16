from .models import Author, Quote, Content
from taggit.models import Tag
from django.conf import settings
from django.db.models import Count


def global_vars(request):
	CONTENT = Content.objects.all()
	AUTHORS = Author.objects.all().order_by('name')
	SIDEBAR_AUTHORS = Author.objects.annotate(num_quotes=Count('quotes')).order_by('-num_quotes')
	SIDEBAR_TOPICS = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')
	#RANDOM_IMAGES = settings.RANDOM_IMAGES

	return {
		'CONTENT' : CONTENT,
		'AUTHORS' : AUTHORS,
		'SIDEBAR_AUTHORS' : SIDEBAR_AUTHORS,
		'SIDEBAR_TOPICS' : SIDEBAR_TOPICS,
		#'RANDOM_IMAGES' : RANDOM_IMAGES,
	}