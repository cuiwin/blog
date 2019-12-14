from django.contrib import admin
from .models import Article
from .models import Category
from .models import Tag
# Register your models here.

#采用装饰器方式注册
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display=('id','name','created')

    # list_editable 设置默认可编辑字段
    list_editable = ['name']
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display=('id','name')

    # list_editable 设置默认可编辑字段
    list_editable = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    #多对多模型，自定义方法展示。
    def get_tags(self,obj):
        return [ a.name for a in obj.tags.all() ]

    get_tags.short_description = u'文章标签'

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display=('id','category','title','get_tags','viewnum','likenum','author','created','updated')

    list_display_links = ('id','title')

    # list_editable 设置默认可编辑字段
    list_editable = ['created','viewnum']

    filter_horizontal = ('tags',)


    #筛选
    list_filter = ('category__name',)
    date_hierarchy = 'created'

#admin.site.register(Article)
#admin.site.register(Category)
#admin.site.register(Tag)
