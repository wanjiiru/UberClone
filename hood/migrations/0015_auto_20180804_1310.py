# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-04 13:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0014_auto_20180804_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]