# Generated by Django 2.2 on 2019-10-26 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0005_libro_editorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(default='', max_length=80, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='tipo',
            field=models.CharField(default='', max_length=80, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='title',
            field=models.CharField(default='', max_length=80, verbose_name='Titulo'),
        ),
    ]
