# Generated by Django 2.0.9 on 2019-03-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0047_auto_20190325_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='not_travelled',
            field=models.NullBooleanField(),
        ),
    ]