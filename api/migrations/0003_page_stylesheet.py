# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150514_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='stylesheet',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
