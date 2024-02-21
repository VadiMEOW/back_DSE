# Generated by Django 4.2.4 on 2024-02-21 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera_manager', '0002_alter_camera_input_location'),
        ('api', '0024_remove_zonestats_camera_zonestats_location_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CameraStats',
            new_name='CameraStat',
        ),
        migrations.RenameModel(
            old_name='ZoneStats',
            new_name='ZoneStat',
        ),
        migrations.RemoveField(
            model_name='objectsdetectionlog',
            name='location',
        ),
        migrations.RemoveField(
            model_name='objectsdetectionlog',
            name='type',
        ),
        migrations.DeleteModel(
            name='DetectedObjectType',
        ),
        migrations.DeleteModel(
            name='ObjectsDetectionLog',
        ),
    ]
