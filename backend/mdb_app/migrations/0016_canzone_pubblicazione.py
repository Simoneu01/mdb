# Generated by Django 3.0.6 on 2020-05-23 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mdb_app', '0015_auto_20200523_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='canzone',
            name='pubblicazione',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
