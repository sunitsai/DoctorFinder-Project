# Generated by Django 3.1.4 on 2020-12-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201227_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='birthdate',
            field=models.DateField(blank=True, default='2020-06-27'),
        ),
    ]
