# Generated by Django 2.0.9 on 2019-03-16 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opal', '0037_auto_20181114_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinical_info', models.TextField(blank=True)),
                ('datetime_ordered', models.DateTimeField(blank=True, null=True)),
                ('site', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(blank=True, max_length=256, null=True)),
                ('test_code', models.CharField(blank=True, max_length=256, null=True)),
                ('test_name', models.CharField(blank=True, max_length=256, null=True)),
                ('lab_number', models.CharField(blank=True, max_length=256, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_tests', to='opal.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('observation_datetime', models.DateTimeField(blank=True, null=True)),
                ('observation_name', models.CharField(blank=True, max_length=256, null=True)),
                ('observation_number', models.CharField(blank=True, max_length=256, null=True)),
                ('observation_value', models.TextField(blank=True)),
                ('reference_range', models.CharField(blank=True, max_length=256, null=True)),
                ('units', models.CharField(blank=True, max_length=256, null=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labtests.LabTest')),
            ],
        ),
    ]
