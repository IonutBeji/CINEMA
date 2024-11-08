# Generated by Django 5.1.1 on 2024-11-03 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0002_rename_active_location_activate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_movie', models.CharField(max_length=100)),
                ('anul_lansarii', models.CharField(max_length=100)),
                ('nominalizari', models.CharField(max_length=100)),
                ('premii', models.CharField(max_length=100)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
            ],
        ),
    ]
