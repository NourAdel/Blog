# Generated by Django 2.2.5 on 2019-10-12 13:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20191012_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2019, 10, 12, 13, 21, 25, 457947, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
