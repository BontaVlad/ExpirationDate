# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('birth_date', models.DateField(null=True, verbose_name='birth date', blank=True)),
                ('date_of_death', models.DateField(null=True, verbose_name='date of death', blank=True)),
                ('birth_place', models.CharField(max_length=100, verbose_name='birth place', blank=True)),
                ('funeral_date', models.DateTimeField(null=True, verbose_name='funeral date', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name='address', blank=True)),
                ('postcode', models.CharField(max_length=10, verbose_name='postcode', help_text='(e.g.:1234 AB)', blank=True)),
                ('phone', models.CharField(max_length=20, verbose_name='phone', blank=True)),
                ('mobile', models.CharField(max_length=20, verbose_name='mobile', blank=True)),
                ('gender', models.PositiveSmallIntegerField(default=0, verbose_name='gender', choices=[(0, 'Not specified'), (1, 'Male'), (2, 'Female')], help_text='Indicates the gender of the user.')),
                ('religion', models.PositiveSmallIntegerField(default=0, verbose_name='religion', choices=[(0, 'Not specified'), (1, 'Christianity'), (2, 'Islam'), (3, 'Hinduism'), (4, 'Buddhism')], help_text='Indicates the religion of the user.')),
                ('is_deceased', models.BooleanField(default=False, verbose_name='is deceased')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
