# Generated by Django 3.0.5 on 2020-06-01 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200602_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='catlist',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='editor',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='hotnews',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='suggested',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tech',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='trending',
            name='slug',
        ),
    ]