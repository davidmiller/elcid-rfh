# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-08 16:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elcid', '0016_auto_20171212_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antimicrobial',
            name='adverse_event_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Antimicrobial_adverse_event'),
        ),
        migrations.AlterField(
            model_name='antimicrobial',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_antimicrobial_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='antimicrobial',
            name='delivered_by_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.Drug_delivered'),
        ),
        migrations.AlterField(
            model_name='antimicrobial',
            name='drug_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Antimicrobial'),
        ),
        migrations.AlterField(
            model_name='antimicrobial',
            name='frequency_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Antimicrobial_frequency'),
        ),
        migrations.AlterField(
            model_name='antimicrobial',
            name='reason_for_stopping_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.Iv_stop'),
        ),
        migrations.AlterField(
            model_name='antimicrobial',
            name='route_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Antimicrobial_route'),
        ),
        migrations.AlterField(
            model_name='antimicrobial',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_antimicrobial_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='birth_place_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Destination'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_demographics_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='ethnicity_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Ethnicity'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='marital_status_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.MaritalStatus'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='sex_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Gender'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='title_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Title'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_demographics_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='condition_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Condition'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_diagnosis_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_diagnosis_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='duplicatepatient',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_duplicatepatient_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='duplicatepatient',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_duplicatepatient_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='finaldiagnosis',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_finaldiagnosis_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='finaldiagnosis',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_finaldiagnosis_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='imaging',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_imaging_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='imaging',
            name='imaging_type_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.ImagingTypes'),
        ),
        migrations.AlterField(
            model_name='imaging',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_imaging_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='infection',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_infection_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='infection',
            name='source_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.InfectionSource'),
        ),
        migrations.AlterField(
            model_name='infection',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_infection_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='line',
            name='complications_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Line_complication'),
        ),
        migrations.AlterField(
            model_name='line',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_line_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='line',
            name='line_type_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Line_type'),
        ),
        migrations.AlterField(
            model_name='line',
            name='removal_reason_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Line_removal_reason'),
        ),
        migrations.AlterField(
            model_name='line',
            name='site_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Line_site'),
        ),
        migrations.AlterField(
            model_name='line',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_line_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='category_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.LocationCategory'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_location_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='hospital_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Hospital'),
        ),
        migrations.AlterField(
            model_name='location',
            name='provenance_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.Provenance'),
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_location_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='ward_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Ward'),
        ),
        migrations.AlterField(
            model_name='microbiologyinput',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_microbiologyinput_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='microbiologyinput',
            name='liver_function_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.LiverFunction'),
        ),
        migrations.AlterField(
            model_name='microbiologyinput',
            name='reason_for_interaction_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Clinical_advice_reason_for_interaction'),
        ),
        migrations.AlterField(
            model_name='microbiologyinput',
            name='renal_function_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.RenalFunction'),
        ),
        migrations.AlterField(
            model_name='microbiologyinput',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_microbiologyinput_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='positivebloodculturehistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_positivebloodculturehistory_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='positivebloodculturehistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_positivebloodculturehistory_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='primarydiagnosis',
            name='condition_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.PrimaryDiagnosisCondition'),
        ),
        migrations.AlterField(
            model_name='primarydiagnosis',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_primarydiagnosis_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='primarydiagnosis',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_primarydiagnosis_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_procedure_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='medical_procedure_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.MedicalProcedure'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='surgical_procedure_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.SurgicalProcedure'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_procedure_subrecords', to=settings.AUTH_USER_MODEL),
        ),
    ]