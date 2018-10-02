# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-15 20:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0034_auto_20171214_1845'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tb', '0028_pregnancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='TBAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('state', models.CharField(blank=True, default=b'', max_length=256)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('clinic_resource', models.CharField(blank=True, default=b'', max_length=256)),
                ('location', models.CharField(blank=True, default=b'', max_length=256)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tb_tbappointment_subrecords', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_tb_tbappointment_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.AlterModelOptions(
            name='bcg',
            options={'verbose_name': 'BCG'},
        ),
        migrations.AlterModelOptions(
            name='contactdetails',
            options={'verbose_name': 'Contact Details', 'verbose_name_plural': 'Contact Details'},
        ),
        migrations.AlterModelOptions(
            name='nextofkin',
            options={'verbose_name': 'Next Of Kin', 'verbose_name_plural': 'Next Of Kin'},
        ),
        migrations.AlterModelOptions(
            name='patientconsultation',
            options={'verbose_name': 'Patient Consultation'},
        ),
        migrations.AlterModelOptions(
            name='socialhistory',
            options={'verbose_name': 'Social History', 'verbose_name_plural': 'Social Histories'},
        ),
        migrations.AlterModelOptions(
            name='tbhistory',
            options={'verbose_name': 'History of TB', 'verbose_name_plural': 'History of TB'},
        ),
        migrations.AlterModelOptions(
            name='travel',
            options={'verbose_name': 'Travel History', 'verbose_name_plural': 'Travel Histories'},
        ),
        migrations.AlterField(
            model_name='employment',
            name='financial_status',
            field=models.CharField(blank=True, choices=[(b'Nil income', b'Nil income'), (b'On benefits', b'On benefits'), (b'Other(SS/NASS)', b'Other(SS/NASS)'), (b'Employed', b'Employed')], max_length=256),
        ),
    ]