# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('type', models.CharField(max_length=1, null=True, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'unnamed', max_length=50)),
                ('armor', models.ForeignKey(related_name='armorPart', default=b'31', to='robotApp.Part')),
                ('power', models.ForeignKey(related_name='powerPart', default=b'18', to='robotApp.Part')),
                ('propulsion', models.ForeignKey(related_name='propPart', default=b'7', to='robotApp.Part')),
                ('weapons', models.ManyToManyField(related_name='weaponPart', to='robotApp.Part', blank=True)),
            ],
        ),
    ]
