# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171208_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True, unique=True),
        ),
    ]
