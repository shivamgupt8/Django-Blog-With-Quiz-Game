# Generated by Django 3.0.5 on 2020-05-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200505_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sets',
            name='set_topic',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]