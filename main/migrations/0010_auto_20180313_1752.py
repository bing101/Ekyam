# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-13 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180313_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incubators',
            old_name='varify',
            new_name='verify',
        ),
        migrations.AlterField(
            model_name='incubators',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
