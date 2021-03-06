# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-20 18:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(max_length=30)),
                ('startup_product', models.CharField(max_length=30)),
                ('startup_date', models.DateField(auto_now=True)),
                ('startup_sector', models.CharField(max_length=30)),
                ('startup_team_size', models.IntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)])),
                ('startup_desc', models.TextField(max_length=1200)),
                ('startup_team_condition', models.BooleanField(default=True)),
                ('startup_team', models.CharField(max_length=200)),
            ],
        ),
    ]
