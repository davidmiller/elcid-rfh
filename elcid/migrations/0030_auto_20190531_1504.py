# Generated by Django 2.0.13 on 2019-05-31 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0037_auto_20181114_1445'),
        ('elcid', '0029_auto_20190418_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodCultureIsolate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('aerobic_or_anaerobic', models.CharField(blank=True, choices=[('Aerobic', 'Aerobic'), ('Anaerobic', 'Anaerobic')], max_length=256, null=True, verbose_name='Blood culture bottle type')),
                ('notes', models.TextField(blank=True)),
                ('quick_fish_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('gpc_staph_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('organism_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('sepsityper_organism_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('gram_stain_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('gpc_strep_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BloodCultureSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('date_ordered', models.DateField(blank=True, null=True)),
                ('date_positive', models.DateField(blank=True, null=True)),
                ('lab_number', models.CharField(blank=True, max_length=256, null=True)),
                ('source_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_bloodcultureset_subrecords', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient')),
                ('source_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.BloodCultureSource')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_bloodcultureset_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blood Cultures',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GNROutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GPCStaphOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GPCStrepOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GramStainOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuickFishOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='quickfishoutcome',
            unique_together={('code', 'system')},
        ),
        migrations.AlterUniqueTogether(
            name='gramstainoutcome',
            unique_together={('code', 'system')},
        ),
        migrations.AlterUniqueTogether(
            name='gpcstrepoutcome',
            unique_together={('code', 'system')},
        ),
        migrations.AlterUniqueTogether(
            name='gpcstaphoutcome',
            unique_together={('code', 'system')},
        ),
        migrations.AlterUniqueTogether(
            name='gnroutcome',
            unique_together={('code', 'system')},
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='blood_culture_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isolates', to='elcid.BloodCultureSet'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_elcid_bloodcultureisolate_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='gpc_staph_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.GPCStaphOutcome'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='gpc_strep_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.GPCStrepOutcome'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='gram_stain_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.GramStainOutcome'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='organism_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Microbiology_organism'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='quick_fish_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='elcid.QuickFishOutcome'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='resistance',
            field=models.ManyToManyField(blank=True, related_name='resistant_isolates', to='opal.Antimicrobial'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='sensitivities',
            field=models.ManyToManyField(blank=True, related_name='sensitive_isolates', to='opal.Antimicrobial'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='sepsityper_organism_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sepsityper_organism', to='opal.Microbiology_organism'),
        ),
        migrations.AddField(
            model_name='bloodcultureisolate',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_elcid_bloodcultureisolate_subrecords', to=settings.AUTH_USER_MODEL),
        ),
    ]