# Generated by Django 2.2.4 on 2019-10-21 03:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20191020_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 21, 3, 17, 32, 768790, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
