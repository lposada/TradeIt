# Generated by Django 2.2.4 on 2019-10-16 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20191008_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='trueques',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='', max_length=30, verbose_name='Apellido'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='saldo',
            field=models.SmallIntegerField(default=0, verbose_name='Saldo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=80, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(default='', max_length=80, verbose_name='Tipo'),
        ),
    ]