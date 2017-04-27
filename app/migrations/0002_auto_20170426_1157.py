# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_by',
            field=models.ForeignKey(related_name='done_by_r', to='app.UserProfile', blank=True),
        ),
    ]
