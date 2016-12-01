# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisingplus', '0004_auto_20161201_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='docType',
        ),
        migrations.AddField(
            model_name='document',
            name='doc',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='docname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
