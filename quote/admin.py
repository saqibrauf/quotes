from django.contrib import admin
from .models import Author, Quote



class AuthorAdmin(admin.ModelAdmin):
	search_fields = ['author_name']


class QuoteAdmin(admin.ModelAdmin):
	autocomplete_fields = ['author_name']
	list_display = ('quote', 'author_name')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)