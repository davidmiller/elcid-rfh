# Generated by Django 2.0.13 on 2020-02-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elcid', '0032_auto_20190617_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='antimicrobial',
            name='treatment_reason',
            field=models.CharField(blank=True, choices=[('Empiric', 'Empiric'), ('Targetted', 'Targetted'), ('Pre-emptive', 'Pre-emptive')], max_length=256, null=True),
        ),
    ]
