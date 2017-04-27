# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170426_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_by',
            field=models.ForeignKey(null=True, blank=True, related_name='done_by_r', to='app.UserProfile'),
        ),
    ]
