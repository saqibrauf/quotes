from django.contrib import admin
from .models import Author, Quote
from django.template.defaultfilters import slugify
from taggit.models import Tag



class AuthorAdmin(admin.ModelAdmin):
	search_fields = ['name']
	def total_quotes(self, obj):
		author = Author.objects.get(id=obj.id)
		total = author.quotes.count()
		return total
	list_display = ['name', 'total_quotes']

class QuoteAdmin(admin.ModelAdmin):
	autocomplete_fields = ['author', 'tags']
	list_display = ('quote', 'slug', 'author', 'user')
	exclude = ['user']
	search_fields = ['quote']

	def save_model(self, request, obj, form, change):
	    obj.slug = slugify(obj.quote[:100])
	    obj.user = request.user
	    super().save_model(request, obj, form, change)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)