from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    """
    栏目的Model
    """
    name    = models.CharField("文章分类名称",max_length=50,blank=True)
    created = models.DateTimeField("创建时间",default=timezone.now)

    class Meta:
        db_table = 'blog_category'
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    文章的标签
    """
    name  = models.CharField("文章标签名",max_length=30)

    class Meta:
        db_table = 'blog_tag'
        verbose_name = "标签"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name

class Article(models.Model):
    """
    文章的Model
    """
    author      = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="文章作者")
    category    = models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE,verbose_name="文章分类")
    tags        = models.ManyToManyField(Tag,blank=True,verbose_name="文章标签")
    title       = models.CharField("文章标题",max_length=100)
    brief       = models.CharField("文件简介",max_length=200)
    body        = models.TextField("文章内容")
    avatar      = models.ImageField("文章配图",upload_to='article/%Y%m%d/',blank=True)
    viewnum     = models.PositiveIntegerField("浏览量",default=0)
    likenum     = models.PositiveIntegerField("点赞数量",default=0)
    created     = models.DateTimeField("创建时间",default=timezone.now)
    updated     = models.DateTimeField("更新时间",auto_now=True)

    class Meta:
        ordering = ['-created']
        db_table = 'blog_article'
        verbose_name = "文章"
        verbose_name_plural = "文章"

