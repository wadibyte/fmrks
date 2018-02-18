# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 08:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marker',
            name='desrc',
        ),
        migrations.AddField(
            model_name='marker',
            name='descr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='marker',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='markers_marker_create_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
