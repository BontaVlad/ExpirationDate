# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
        ('cemeteries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractsRegister',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('current_number', models.BigIntegerField(unique=True, verbose_name='current_number')),
                ('contract_number', models.BigIntegerField(unique=True, verbose_name='contract_number')),
                ('release_date', models.DateTimeField(verbose_name='release_date')),
                ('owner', models.ForeignKey(to='persons.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grave',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', null=True)),
                ('receipt_number', models.BigIntegerField(null=True, verbose_name='receipt_number', blank=True)),
                ('surface_area', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='surface area')),
                ('has_funeral_constructions', models.BooleanField(default=False)),
                ('parcel', models.SmallIntegerField(default=0, verbose_name='parcel')),
                ('row', models.SmallIntegerField(default=0, verbose_name='row')),
                ('position', models.SmallIntegerField(default=0, verbose_name='position')),
                ('social_services_request', models.BigIntegerField(null=True, verbose_name='IML request', blank=True)),
                ('cemetery', models.ForeignKey(to='cemeteries.Cemetery')),
                ('deceased', models.ForeignKey(unique=True, to='persons.Person', blank=True, null=True)),
                ('owner', models.ForeignKey(related_name='graves', to='persons.Person', blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GraveOwnership',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateField(verbose_name='expiration_date')),
                ('owned_grave', models.ForeignKey(related_name='owned_grave', to='registers.Grave')),
                ('person', models.ForeignKey(related_name='person', to='persons.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GraveOwnershipRequestsRegister',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('current_number', models.BigIntegerField(unique=True, verbose_name='current_number')),
                ('registration_date', models.DateTimeField(verbose_name='registration_date')),
                ('infocet_number', models.BigIntegerField(verbose_name='infocet_number')),
                ('status', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Favorable'), (1, 'Not favorable'), (2, 'Partial'), (3, 'Rejected'), (4, 'Internal')], verbose_name='status')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UpcomingFuneral',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('funeral_date', models.DateTimeField(verbose_name='funeral date')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('deceased', models.ForeignKey(related_name='upcomming_funerals', to='persons.Person')),
                ('grave', models.ForeignKey(related_name='grave', to='registers.Grave')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnnualDeathIndexRegister',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('persons.person',),
        ),
        migrations.CreateModel(
            name='AnnualOwnerlessDeathRegister',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
        migrations.CreateModel(
            name='ExpiredGrave',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
        migrations.CreateModel(
            name='FuneralMonument',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
        migrations.CreateModel(
            name='GravesPayedThisYear',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
        migrations.CreateModel(
            name='GravesToExpireThisYear',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.grave',),
        ),
        migrations.CreateModel(
            name='UpcomingFuneralArchive',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('registers.upcomingfuneral',),
        ),
    ]
