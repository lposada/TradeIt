# Generated by Django 2.2 on 2019-10-26 20:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20191026_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 20, 6, 16, 536708, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
