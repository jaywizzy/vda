# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-21 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180220_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='home_address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
