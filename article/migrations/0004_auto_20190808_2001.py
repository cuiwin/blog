# Generated by Django 2.2.2 on 2019-08-08 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190807_2126'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tag',
            table='blog_tag',
        ),
    ]
