# Generated by Django 2.2.4 on 2019-09-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_auto_20190914_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
    ]