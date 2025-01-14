# Generated by Django 5.1.3 on 2024-11-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('package_destination', models.CharField(max_length=200)),
                ('package_description', models.TextField(default='Package Description')),
                ('package_price', models.PositiveIntegerField(default=0)),
                ('package_image', models.ImageField(upload_to='packages/')),
            ],
        ),
    ]
