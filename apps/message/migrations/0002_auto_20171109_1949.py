# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='主键'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.CharField(max_length=500, verbose_name='留言信息'),
        ),
    ]
