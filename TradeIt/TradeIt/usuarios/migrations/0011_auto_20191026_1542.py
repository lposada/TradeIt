# Generated by Django 2.2 on 2019-10-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_auto_20191026_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
    ]
