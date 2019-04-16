# Generated by Django 2.0.9 on 2019-03-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elcid', '0029_auto_20190311_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referralroute',
            name='referral_reason',
            field=models.CharField(blank=True, choices=[('Symptomatic', 'Symptomatic'), ('TB contact screening', 'TB contact screening'), ('New entrant screening', 'New entrant screening'), ('Transferred in TB Rx', 'Transferred in TB Rx'), ('Pre-immunosuppression screening', 'Pre-immunosuppression screening'), ('BCG Vaccination', 'BCG Vaccination'), ('Other', 'Other')], default='', max_length=256),
        ),
    ]