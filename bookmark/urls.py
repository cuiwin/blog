from . import views
from django.urls import path

app_name = "bookmark"

urlpatterns = [
    #收藏首页
    path('',views.IndexView.as_view(),name='index'),

    #收藏关于页
    path('bookmark_about/', views.bookmark_about, name='bookmark_about'),

]