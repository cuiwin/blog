from . import views
from django.urls import path
app_name = "article"

urlpatterns = [
    #文章首页，首页和列表目前一样
    path('',views.article_list,name='index'),
    #文章列表
    path('article_list/',views.article_list,name='article_list'),
    #文章详情
    path('article_detail/<int:id>/',views.article_detail,name='article_detail'),
    #文章点赞
    path('increase-likes/<int:id>/',views.increase_likes,name='increase_likes')
]