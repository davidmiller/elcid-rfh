# Generated by Django 2.0.13 on 2019-04-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0049_auto_20190326_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='additional_exposures',
            field=models.TextField(default=''),
        ),
    ]