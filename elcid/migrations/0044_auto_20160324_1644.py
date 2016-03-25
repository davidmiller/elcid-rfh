# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elcid', '0043_update_demographic_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demographics',
            old_name='country_of_birth_fk',
            new_name='birth_place_fk',
        ),
        migrations.RenameField(
            model_name='demographics',
            old_name='country_of_birth_ft',
            new_name='birth_place_ft',
        ),
    ]
