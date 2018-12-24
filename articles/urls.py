from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.articlelist,name="list"),
    path('create/',views.create_article,name="create"),
    path('<slug:title>',views.article_detail,name="detail"),
]