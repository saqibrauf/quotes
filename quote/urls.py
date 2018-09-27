from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('quote/<slug>', views.quote, name = 'quote'),
    path('author/<slug>', views.author, name = 'author'),
    path('tag/<slug>', views.tag, name = 'tag'),
]