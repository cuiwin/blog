# Generated by Django 2.2.2 on 2019-12-07 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_auto_20191117_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': '链接', 'verbose_name_plural': '链接'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
    ]
