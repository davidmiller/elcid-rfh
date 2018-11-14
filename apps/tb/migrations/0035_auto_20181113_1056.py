# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0034_auto_20180824_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbmanagement',
            options={'verbose_name': 'TB Management'},
        ),
        migrations.AddField(
            model_name='lymphnodeswellingsiteoptions',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lymphnodeswellingsiteoptions',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lymphnodeswellingsiteoptions',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recreationaldrug',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recreationaldrug',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recreationaldrug',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbcasemanager',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbcasemanager',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbcasemanager',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbsite',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbsite',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbsite',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbtreatmentcentre',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbtreatmentcentre',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tbtreatmentcentre',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tbmanagement',
            name='ltbr_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name=b'LTBR Number'),
        ),
        migrations.AlterUniqueTogether(
            name='lymphnodeswellingsiteoptions',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='recreationaldrug',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='tbcasemanager',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='tbsite',
            unique_together=set([('code', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='tbtreatmentcentre',
            unique_together=set([('code', 'system')]),
        ),
    ]
