# Generated by Django 2.2.5 on 2019-09-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190925_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='-', unique=True),
        ),
    ]
