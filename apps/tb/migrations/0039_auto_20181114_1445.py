# Generated by Django 2.0.9 on 2018-11-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0038_auto_20181114_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergies',
            name='provisional',
            field=models.BooleanField(default=False, help_text='True if the allergy is only suspected. Defaults to False.', verbose_name='Suspected?'),
        ),
        migrations.AlterField(
            model_name='patientconsultation',
            name='initials',
            field=models.CharField(blank=True, help_text='The initials of the user who gave the consult.', max_length=255),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='start_date',
            field=models.DateField(blank=True, help_text='The date on which the patient began receiving this treatment.', null=True),
        ),
    ]
