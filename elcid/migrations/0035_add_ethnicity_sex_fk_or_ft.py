# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0011_patientrecordaccess'),
        ('elcid', '0034_gloss_demographics_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demographics',
            old_name='ethnicity_old ',
            new_name='ethnicity_old',
        ),
        migrations.AddField(
            model_name='demographics',
            name='ethnicity_fk',
            field=models.ForeignKey(blank=True, to='opal.Ethnicity', null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='ethnicity_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='sex_fk',
            field=models.ForeignKey(blank=True, to='opal.Gender', null=True),
        ),
        migrations.AddField(
            model_name='demographics',
            name='sex_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
