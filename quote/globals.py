from .models import Author, Quote


def authors(request):
	authors = Author.objects.all().order_by('name')

	return {
		'AUTHORS' : authors,
	}