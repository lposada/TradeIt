# Generated by Django 2.2 on 2019-10-26 20:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0037_auto_20191026_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 20, 47, 2, 732919, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]