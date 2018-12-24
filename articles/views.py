from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.

def articlelist(request):
	articles = Article.objects.all().order_by('date')
	return render(request,'articles/article_list.html',{'articles':articles})

def article_detail(request,title):
	article  = Article.objects.get(slug=title)
	#return HttpResponse(title)
	return render(request,'articles/article_detail.html',{'article':article})

