# Generated by Django 5.1.1 on 2024-11-02 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='active',
            new_name='activate',
        ),
    ]
