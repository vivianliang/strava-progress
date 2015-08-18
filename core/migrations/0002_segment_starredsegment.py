# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StarredSegment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('segment', models.ForeignKey(related_name='+', to='core.Segment')),
                ('user', models.ForeignKey(related_name='starred_segments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
