# Generated by Django 2.2.5 on 2019-09-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
