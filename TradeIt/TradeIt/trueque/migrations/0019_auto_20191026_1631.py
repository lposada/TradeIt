# Generated by Django 2.2 on 2019-10-26 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trueque', '0018_auto_20191026_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trueque',
            name='libro',
        ),
        migrations.RemoveField(
            model_name='trueque',
            name='usuario',
        ),
    ]