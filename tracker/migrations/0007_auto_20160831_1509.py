# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20160831_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='crqtable',
            name='DeliveryDate',
            field=models.DateField(blank=True, help_text='Delivery Date', null=True),
        ),
        migrations.AddField(
            model_name='crqtable',
            name='Stage',
            field=models.CharField(default='Initiated', help_text='CRQ Stage', max_length=15),
        ),
    ]