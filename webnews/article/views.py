from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

#view function
from .models import Article

def greet(request):
    return HttpResponse("<H1> Hello pnv!<H1>")


def get_one_article(request):

     obj=Article.objects.first()
     context={'article':obj}
     return render(request, 'frontpage.html',context)

def get_all_articles(request):

     objs= Article.objects.all()
     context={'all_articles':objs}
     return (request, 'all.html', context)
