# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-21 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20180221_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
    ]
