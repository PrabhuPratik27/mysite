from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.articlelist,name="list"),
    path('<slug:title>',views.article_detail,name="detail"),
]