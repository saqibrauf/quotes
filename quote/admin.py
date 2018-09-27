from django.contrib import admin
from .models import Author, Quote, Tag



class AuthorAdmin(admin.ModelAdmin):
	search_fields = ['author_name']


class TagAdmin(admin.ModelAdmin):
	search_fields = ['tag_name']


class QuoteAdmin(admin.ModelAdmin):
	autocomplete_fields = ['author_name', 'tags']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Quote, QuoteAdmin)