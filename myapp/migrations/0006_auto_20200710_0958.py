# Generated by Django 3.0.7 on 2020-07-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200709_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='xinli',
            name='topic',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='xinli',
            name='url',
            field=models.CharField(default='', max_length=128),
        ),
    ]