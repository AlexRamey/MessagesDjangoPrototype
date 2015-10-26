# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_private_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='private_message',
            name='sent_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 26, 16, 31, 23, 834171, tzinfo=utc), verbose_name='date sent'),
        ),
    ]
