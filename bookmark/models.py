from django.db import models


class Topic(models.Model):
    """
    收藏夹主题
    """
    name     = models.CharField("收藏主题名称",max_length=50)
    parent   = models.ForeignKey('self',verbose_name="父主题",on_delete=models.SET_NULL,null=True,blank=True)
    ishot    = models.BooleanField("是否推荐")
    icon     = models.CharField("图标名称",max_length=30)

    class Meta:
        db_table = "bookmark_topic"
        verbose_name = "分类"
        verbose_name_plural = "分类"


    def __str__(self):
        return self.name

class Link(models.Model):
    """
    收藏链接
    """
    name  = models.CharField("链接名称",max_length=50)
    info  = models.CharField("链接简介",max_length=100)
    url   = models.CharField("链接URL",max_length=100)
    pic   = models.ImageField("链接配图",upload_to='bookmarkimg/')
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,verbose_name="链接所属主题")

    class Meta:
        db_table = "bookmark_link"
        verbose_name = "链接"
        verbose_name_plural = "链接"