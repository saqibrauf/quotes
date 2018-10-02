from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('quote/<slug>', views.quote, name = 'quote'),
    path('quotes-of-<slug>', views.author, name = 'author'),
    path('<slug>-quotes', views.tag, name = 'tag'),
]