# Generated by Django 4.2.4 on 2023-12-14 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camera_manager', '0001_initial'),
        ('processing', '0011_alter_processaction_action_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='camera_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camera_manager.camera'),
        ),
    ]