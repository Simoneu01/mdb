# Generated by Django 3.0.6 on 2020-05-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdb_app', '0012_auto_20200523_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='generi',
            field=models.ManyToManyField(blank=True, to='mdb_app.Genere'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='generi',
            field=models.ManyToManyField(blank=True, to='mdb_app.Genere'),
        ),
    ]