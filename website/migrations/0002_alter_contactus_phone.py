# Generated by Django 5.0.1 on 2024-01-16 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
