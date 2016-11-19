# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advisingplus', '0002_notes_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor_Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='sessionId',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.AddField(
            model_name='session',
            name='Advisor_Timeslot',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='advisingplus.Advisor_Timeslot'),
            preserve_default=False,
        ),
    ]
