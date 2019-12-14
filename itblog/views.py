# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from article.models import  Article
from article.models import Category
from article.models import Tag


# 首页
def index(request):
    # 初始化查询集
    articles = Article.objects.all()

    # 文章分页
    paginator = Paginator(articles,6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    # 初始化分类查询集
    categorys = Category.objects.all()

    # 初始化标签查询集
    tags = Tag.objects.all()

    context = { 'articles':articles,'categorys':categorys,'tags':tags}
    return render(request,'index.html',context)

# 关于我
def about(request):
    return render(request, 'about.html')