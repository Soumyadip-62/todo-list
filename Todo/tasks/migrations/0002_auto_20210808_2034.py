# Generated by Django 3.1.6 on 2021-08-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='g_date',
            field=models.DateField(blank=True),
        ),
    ]
