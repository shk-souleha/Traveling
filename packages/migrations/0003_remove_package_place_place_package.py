# Generated by Django 5.1.3 on 2024-11-14 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_place_package_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='place',
        ),
        migrations.AddField(
            model_name='place',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='packages.package'),
        ),
    ]
