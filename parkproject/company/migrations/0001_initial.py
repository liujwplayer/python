# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-26 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=100)),
                ('company_size', models.CharField(max_length=10)),
                ('company_time', models.DateTimeField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
