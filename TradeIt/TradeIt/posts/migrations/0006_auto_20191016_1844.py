# Generated by Django 2.2.4 on 2019-10-16 23:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20191016_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 16, 23, 44, 38, 828902, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
