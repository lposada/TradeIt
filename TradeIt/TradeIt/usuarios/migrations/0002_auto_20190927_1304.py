# Generated by Django 2.2.4 on 2019-09-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['-created'], 'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AddField(
            model_name='usuario',
            name='trueques',
            field=models.SmallIntegerField(default=0, verbose_name='Trueques'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.SmallIntegerField(default=0, primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
    ]