# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Effort',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('elapsed_time', models.IntegerField()),
                ('moving_time', models.IntegerField()),
                ('start_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(related_name='profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('pic', models.URLField()),
            ],
        ),
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
        migrations.AddField(
            model_name='effort',
            name='segment',
            field=models.ForeignKey(related_name='efforts', to='core.Segment'),
        ),
        migrations.AddField(
            model_name='effort',
            name='user',
            field=models.ForeignKey(related_name='efforts', to=settings.AUTH_USER_MODEL),
        ),
    ]
