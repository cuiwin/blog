from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article
from .models import Category
from .models import Tag
import markdown

# 文章列表的函数视图
def article_list(request):
    categoryId   = request.GET.get('category')
    tagId        = request.GET.get('tag')
    searchstr    = request.POST.get('searchstr')

    # 初始化查询集
    articles = Article.objects.all()

    if categoryId is not None and categoryId.isdigit():
        articles = articles.filter(category=categoryId)
    if tagId is not None:
        articles = articles.filter(tags=tagId)
    if searchstr is not None:
        articles = articles.filter(
            Q(title__icontains=searchstr) |
            Q(body__icontains=searchstr)
        )

    # 文章分页
    paginator = Paginator(articles,5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    # 初始化分类查询集
    categorys = Category.objects.all()

    # 初始化标签查询集
    tags = Tag.objects.all()

    context = {
        'articles':articles,
        'categorys':categorys,
        'tags':tags,
        'searchstr': searchstr
    }
    return render(request,'article/list.html',context)

# 文章详情页的函数视图
def article_detail(request,id):
    article = Article.objects.get(id=id)

    #浏览量增加
    article.viewnum += 1
    article.save(update_fields=['viewnum'])

    # markdown语法渲染html样式
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )

    #获取上一篇文章列表
    prelist = Article.objects.filter(category__name=article.category).filter(id__lt=article.id).order_by('-id')

    #获取下一篇文章列表
    nextlist = Article.objects.filter(category__name=article.category).filter(id__gt=article.id).order_by('id')

    if prelist.count() > 0:
        pre_article = prelist[0]
    else:
        pre_article = None

    if nextlist.count() > 0:
        next_article = nextlist[0]
    else:
        next_article = None


    article.body = md.convert(article.body)
    context = { 'article':article,'toc':md.toc,'pre_article':pre_article,'next_article':next_article }
    return render(request,'article/detail.html',context)


# 文章点赞
def increase_likes(request,id):
    article = Article.objects.get(id=id)
    article.likenum += 1
    article.save()
    return HttpResponse("success")