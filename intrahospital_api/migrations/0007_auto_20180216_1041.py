# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-16 10:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intrahospital_api', '0006_patientload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialpatientload',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_intrahospital_api_initialpatientload_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='initialpatientload',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_intrahospital_api_initialpatientload_subrecords', to=settings.AUTH_USER_MODEL),
        ),
    ]