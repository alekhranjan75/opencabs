# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0006_auto_20170321_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='travel_datetime',
        ),
    ]
