# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chassis',
            fields=[
                ('part_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='robotApp.Part')),
                ('weight_capacity', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
            ],
            bases=('robotApp.part',),
        ),
        migrations.AddField(
            model_name='robot',
            name='chassis',
            field=models.ForeignKey(default=b'2', to='robotApp.Chassis'),
        ),
    ]
