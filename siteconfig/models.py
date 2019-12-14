from django.db import models

# Create your models here.

class Config(models.Model):
    """
    网站基本信息
    """
    name        = models.CharField("网站名称",max_length=30,blank=True)
    logo        = models.ImageField("网站Logo",upload_to='config/')
    copyright   = models.CharField("CopyRight文字",max_length=30,blank=True)
    title       = models.CharField("网站标题",max_length=30,blank=True)
    keywords    = models.CharField("网站关键字",max_length=200,blank=True)
    description = models.CharField("网站描述",max_length=200,blank=True)

    linklogo    =  models.ImageField("搜藏夹网站Logo",upload_to='config/')

    class Meta:
        db_table = 'blog_config'
        verbose_name = "网站基本信息"
        verbose_name_plural = "网站基本信息"