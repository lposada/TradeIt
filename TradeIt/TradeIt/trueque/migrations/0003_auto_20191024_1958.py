# Generated by Django 2.2 on 2019-10-25 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trueque', '0002_auto_20191024_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trueque',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
    ]