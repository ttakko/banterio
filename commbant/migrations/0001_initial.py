# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('name', models.TextField(unique=True)),
                ('members', models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL)),
                ('moderator', models.ForeignKey(related_name='mode', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.TextField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('group', models.ForeignKey(related_name='messages', to='commbant.Group')),
            ],
        ),
    ]
