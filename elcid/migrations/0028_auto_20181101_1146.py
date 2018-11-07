# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-01 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elcid', '0027_auto_20181029_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodculturesource',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bloodculturesource',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bloodculturesource',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='consultant',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='consultant',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='consultant',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='drug_delivered',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='drug_delivered',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='drug_delivered',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='imagingtypes',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='imagingtypes',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='imagingtypes',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='infectionsource',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='infectionsource',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='infectionsource',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iv_stop',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iv_stop',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iv_stop',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='liverfunction',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='liverfunction',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='liverfunction',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='locationcategory',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='locationcategory',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='locationcategory',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='medicalprocedure',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='medicalprocedure',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='medicalprocedure',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='primarydiagnosiscondition',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='primarydiagnosiscondition',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='primarydiagnosiscondition',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='provenance',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='provenance',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='provenance',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='renalfunction',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='renalfunction',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='renalfunction',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='surgicalprocedure',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='surgicalprocedure',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='surgicalprocedure',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='bloodculturesource',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='consultant',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='imagingtypes',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='infectionsource',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='liverfunction',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='locationcategory',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='medicalprocedure',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='primarydiagnosiscondition',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='provenance',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='renalfunction',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='surgicalprocedure',
            unique_together=set([('code', 'system')]),
        ),
    ]