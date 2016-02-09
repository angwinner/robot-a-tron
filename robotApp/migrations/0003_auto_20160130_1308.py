# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotApp', '0002_auto_20160129_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='weapons',
        ),
        migrations.AddField(
            model_name='robot',
            name='weapon1',
            field=models.ForeignKey(related_name='weapon1Part', default=b'23', to='robotApp.Part'),
        ),
        migrations.AddField(
            model_name='robot',
            name='weapon2',
            field=models.ForeignKey(related_name='weapon2Part', blank=True, to='robotApp.Part', null=True),
        ),
    ]
