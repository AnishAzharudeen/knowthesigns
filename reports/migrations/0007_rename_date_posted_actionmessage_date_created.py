# Generated by Django 4.2.18 on 2025-01-18 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_rename_worker_id_actionmessage_worker_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actionmessage',
            old_name='date_posted',
            new_name='date_created',
        ),
    ]
