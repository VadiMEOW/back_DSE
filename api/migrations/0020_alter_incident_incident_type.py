# Generated by Django 4.2.4 on 2024-02-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_incident_incident_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='incident_type',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]