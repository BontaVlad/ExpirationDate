# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cemetery',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='cemetery name')),
                ('address', models.CharField(max_length=200, verbose_name='address', blank=True)),
                ('postcode', models.CharField(max_length=10, verbose_name='postcode', help_text='(e.g.:1234 AB)', blank=True)),
                ('phone', models.CharField(max_length=20, verbose_name='phone', blank=True)),
                ('mobile', models.CharField(max_length=20, verbose_name='mobile', blank=True)),
            ],
            options={
                'verbose_name_plural': 'cemeteries',
            },
            bases=(models.Model,),
        ),
    ]
