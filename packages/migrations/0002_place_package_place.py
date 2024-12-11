# Generated by Django 5.1.3 on 2024-11-13 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('place_destination', models.CharField(max_length=200)),
                ('place_description', models.TextField(default='Package Description')),
                ('place_price', models.PositiveIntegerField(default=0)),
                ('place_image', models.ImageField(upload_to='packages/')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='packages.place'),
        ),
    ]