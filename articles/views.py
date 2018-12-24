from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='accounts:login')
def articlelist(request):
	articles = Article.objects.all().order_by('date')
	return render(request,'articles/article_list.html',{'articles':articles})

@login_required(login_url='accounts:login')
def article_detail(request,title):
	article  = Article.objects.get(slug=title)
	#return HttpResponse(title)
	return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url='accounts:login')
def create_article(request):
	return render(request,'articles/article_create.html')

