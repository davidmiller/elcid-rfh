# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-23 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intrahospital_api', '0008_auto_20180222_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batchpatientload',
            options={'ordering': ('started',)},
        ),
        migrations.RenameField(
            model_name='batchpatientload',
            old_name='start',
            new_name='started',
        ),
        migrations.RenameField(
            model_name='batchpatientload',
            old_name='stop',
            new_name='stopped',
        ),
        migrations.RenameField(
            model_name='initialpatientload',
            old_name='start',
            new_name='started',
        ),
        migrations.RenameField(
            model_name='initialpatientload',
            old_name='stop',
            new_name='stopped',
        ),
    ]
