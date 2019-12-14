# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
from article.models import Article,Category
from django.contrib.auth.models import User
import  os
import shutil
import traceback

class Command(BaseCommand):
    help = 'Add blog from markdown file'

    def handle(self, *args, **options):
        user = User.objects.get(id=1)
        cate = Category.objects.get(id=1)

        #指定新文章的保存路径
        markdowndir = "/data/PythonBlog/itblog/markdown/"
        mdlist = os.listdir(markdowndir)
        for filename in mdlist:
            #print(filename)
            #print(filename.split(".")[0])

            # 创建一个文章对象
            article = Article()
            article.title = filename.split(".")[0]

            # 文章作者，默认就是cui用户
            article.author = user

            # 文章的分类，如果存在就保存到之前的里面，如果是新的分类就创建一个分类

            article.category = cate
            article.brief = filename
            article.avatar = "article/20190809/150H2092042-1.jpg"

            with open(markdowndir + filename, 'r') as f:
                article.body = f.read()

            article.save()

            self.stdout.write(self.style.SUCCESS('Successfully create article %s' % article.title ))

            move_file(markdowndir,"/data/historymd/",filename)

"""
文件移动
"""
def move_file(src_path, dst_path, file):
    print ('from : ',src_path)
    print ('to : ',dst_path)
    try:
        # cmd = 'chmod -R +x ' + src_path
        # os.popen(cmd)
        f_src = os.path.join(src_path, file)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        f_dst = os.path.join(dst_path, file)
        shutil.move(f_src, f_dst)
    except Exception as e:
        print ('move_file ERROR: ',e)
        traceback.print_exc()


def create_article():
    pass