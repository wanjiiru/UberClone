# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-04 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0011_auto_20180804_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
            preserve_default=False,
        ),
    ]