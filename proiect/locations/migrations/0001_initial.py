# Generated by Django 5.1.1 on 2024-11-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('projection', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
