# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-13 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0023_auto_20180613_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialhistory',
            name='prison_history_details',
            field=models.TextField(default=b''),
        ),
    ]
