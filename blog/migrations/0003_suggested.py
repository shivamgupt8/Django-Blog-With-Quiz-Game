# Generated by Django 2.2.8 on 2020-04-01 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200401_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggested',
            fields=[
                ('suggested_id', models.IntegerField(primary_key=True, serialize=False)),
                ('suggested_title', models.CharField(max_length=500)),
                ('suggested_logo', models.FileField(upload_to='')),
                ('suggested_author', models.CharField(max_length=500)),
                ('suggested_date', models.CharField(max_length=500)),
                ('suggested_url', models.IntegerField()),
                ('suggested_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
    ]
