# Generated by Django 2.2 on 2019-10-26 21:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0049_auto_20191026_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 21, 27, 6, 835679, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]