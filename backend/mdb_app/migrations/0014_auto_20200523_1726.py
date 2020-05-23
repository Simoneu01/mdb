# Generated by Django 3.0.6 on 2020-05-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdb_app', '0013_auto_20200523_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='canzone',
            name='e_src',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='canzone',
            name='lastfm_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='canzone',
            name='plot',
            field=models.TextField(blank=True, null=True),
        ),
    ]
