from django.contrib import admin
from .models import Topic
from .models import Link
from django.utils.safestring import mark_safe
# Register your models here.

#采用装饰器方式注册
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display=('id','name','parent','ishot','icon')

    # 点击哪些字段可以进入编辑界面
    list_display_links = ('id', 'name')

    # list_editable 设置默认可编辑字段
    list_editable = ['icon']

    #筛选器
    #搜索框
    search_fields = ('name',)
    #过滤器
    list_filter = ('name',)
    #时间分层筛选
    #date_hierarchy = ''

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id','topic','name','info','url','pic_data')

    #定义图片显示
    def pic_data(self,obj):
        return mark_safe('<img src ="%s" width="80px"/>' % obj.pic.url)

    pic_data.short_description = u'链接图片'

    list_display_links = ('id','name')

    #过滤器
    list_filter = ('topic__name',)

    #文本框搜索
    search_fields = ('name',)

    list_editable = ['url']


#在admin后台注册
#admin.site.register(Topic)
#admin.site.register(Link)