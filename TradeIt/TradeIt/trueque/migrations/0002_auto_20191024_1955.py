# Generated by Django 2.2 on 2019-10-25 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trueque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trueque',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
    ]