# Generated by Django 2.2 on 2019-10-27 19:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0056_auto_20191026_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 27, 19, 38, 34, 366816, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]