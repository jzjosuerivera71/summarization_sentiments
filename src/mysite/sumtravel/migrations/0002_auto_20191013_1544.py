# Generated by Django 2.2.5 on 2019-10-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumtravel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudad',
            old_name='id_pais',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='local',
            old_name='id_ciudad',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='local_reviews',
            new_name='local',
        ),
    ]
