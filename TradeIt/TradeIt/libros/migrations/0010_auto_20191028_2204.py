# Generated by Django 2.2 on 2019-10-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0009_auto_20191027_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='Editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='tipo',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='title',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='Titulo'),
        ),
    ]