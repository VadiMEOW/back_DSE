# Generated by Django 4.2.4 on 2024-04-17 05:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0016_alter_process_camera'),
    ]

    operations = [
        migrations.AddField(
            model_name='actiontype',
            name='parameters',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None),
        ),
    ]