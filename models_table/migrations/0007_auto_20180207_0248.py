# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-06 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_table', '0006_auto_20180207_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lmcode',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
