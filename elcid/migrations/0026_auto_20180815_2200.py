# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-15 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elcid', '0025_merge_20180718_0817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='antimicrobial',
            options={'verbose_name': 'Medication History', 'verbose_name_plural': 'Medication Histories'},
        ),
        migrations.AlterModelOptions(
            name='finaldiagnosis',
            options={'verbose_name': 'Final Diagnosis', 'verbose_name_plural': 'Final Diagnoses'},
        ),
        migrations.AlterModelOptions(
            name='infection',
            options={'verbose_name': 'Infection Related Issues'},
        ),
        migrations.AlterModelOptions(
            name='microbiologyinput',
            options={'verbose_name': 'Clinical Advice', 'verbose_name_plural': 'Clinical Advice'},
        ),
        migrations.AlterModelOptions(
            name='pastmedicalhistory',
            options={'verbose_name': 'PMH', 'verbose_name_plural': 'Past medical histories'},
        ),
        migrations.AlterModelOptions(
            name='primarydiagnosis',
            options={'verbose_name': 'Primary Diagnosis', 'verbose_name_plural': 'Primary Diagnoses'},
        ),
        migrations.AlterModelOptions(
            name='procedure',
            options={'verbose_name': 'Operation / Procedures'},
        ),
        migrations.AlterModelOptions(
            name='referralroute',
            options={'verbose_name': 'Referral Route'},
        ),
        migrations.AlterModelOptions(
            name='symptomcomplex',
            options={'verbose_name': 'Symptoms', 'verbose_name_plural': 'Symptom complexes'},
        ),
    ]