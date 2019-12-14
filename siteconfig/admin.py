from django.contrib import admin
from .models import Config
# Register your models here.

#采用装饰器方式注册
@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display=('name','title','keywords','description')

    # 点击哪些字段可以进入编辑界面
    list_display_links = ('name',)

    # list_editable 设置默认可编辑字段
    list_editable = ['title','keywords']
