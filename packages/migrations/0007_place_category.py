# Generated by Django 5.1.3 on 2024-11-18 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='packages.category'),
        ),
    ]
