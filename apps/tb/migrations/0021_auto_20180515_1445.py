# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-15 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0020_auto_20180515_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantouxtest',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mantouxtest',
            name='induration',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Induration (mm)'),
        ),
    ]
