# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-04 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_auto_20180804_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
        ),
    ]
