# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0002_auto_20150311_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewSubmitData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('event_name', models.CharField(max_length=500)),
                ('event_date', models.CharField(max_length=500)),
                ('event_place', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'Submit_Insertdata',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='insertdata',
            name='event_place',
        ),
    ]
