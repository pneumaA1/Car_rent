# Generated by Django 4.1.7 on 2023-03-24 23:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('door_count', models.PositiveIntegerField()),
                ('seats_count', models.PositiveIntegerField()),
                ('transmission', models.CharField(
                    choices=[('automatic', 'Automatic'), ('manual', 'Manual')],
                    max_length=10)),
                ('rating', models.IntegerField(
                    validators=[django.core.validators.MinValueValidator(0),
                                django.core.validators.MaxValueValidator(5)])),
                ('price', models.PositiveIntegerField()),
                ('photo',
                 models.ImageField(blank=True, upload_to='car_photos/')),
            ],
        ),
    ]
