# Generated by Django 3.0.6 on 2020-06-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_movie', '0002_auto_20200601_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Возраст'),
        ),
    ]
