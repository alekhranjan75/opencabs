# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0008_auto_20170331_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_done',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_due',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_email',
            field=models.EmailField(blank=True, db_index=True, default='', max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_mobile',
            field=models.CharField(blank=True, db_index=True, default='', max_length=20, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Name'),
        ),
    ]
