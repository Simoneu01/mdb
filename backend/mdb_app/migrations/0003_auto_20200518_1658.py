# Generated by Django 3.0.6 on 2020-05-18 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdb_app', '0002_auto_20200518_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canzone',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mdb_app.Album'),
        ),
    ]
