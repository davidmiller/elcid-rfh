# Generated by Django 2.0.13 on 2019-05-29 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0037_auto_20181114_1445'),
        ('tb', '0042_tbcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('ltbr_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='LTBR Number')),
                ('hospital_number', models.CharField(blank=True, max_length=200, null=True)),
                ('sputum_smear', models.CharField(blank=True, choices=[('+ve', '+ve'), ('-ve', '-ve'), ('Unknown', 'Unknown')], max_length=200, null=True)),
                ('culture', models.CharField(blank=True, choices=[('+ve', '+ve'), ('-ve', '-ve'), ('Unknown', 'Unknown')], max_length=200, null=True)),
                ('drug_susceptibility', models.CharField(blank=True, choices=[('Fully sensitive', 'Fully sensitive'), ('Not fully sensitive', 'Not fully sensitive'), ('Unknown', 'Unknown')], max_length=200, null=True)),
                ('index_case_diagnosis_years', models.IntegerField(blank=True, null=True)),
                ('index_case_diagnosis_months', models.IntegerField(blank=True, null=True)),
                ('index_case_diagnosis_days', models.IntegerField(blank=True, null=True)),
                ('relationship', models.CharField(blank=True, choices=[('Household', 'Household'), ('Healthcare (workor)', 'Healthcare (worker)'), ('Healthcare (patient)', 'Healthcare (patient)'), ('Workplace (non healthcare)', 'Workplace (non healthcare)'), ('Education', 'Education'), ('Prison', 'Prison')], max_length=200, null=True, verbose_name='Relationship to index case')),
                ('relationship_other', models.CharField(blank=True, max_length=200, null=True)),
                ('details', models.TextField(blank=True)),
                ('index_case_site_of_tb_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tb_indexcase_subrecords', to=settings.AUTH_USER_MODEL)),
                ('index_case_site_of_tb_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tb.TBSite')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_tb_indexcase_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='tbcontact',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tbcontact',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='tbcontact',
            name='updated_by',
        ),
        migrations.AlterModelOptions(
            name='tbhistory',
            options={'verbose_name': 'Personal history of TB', 'verbose_name_plural': 'Personal histories of TB'},
        ),
        migrations.DeleteModel(
            name='TBContact',
        ),
    ]
