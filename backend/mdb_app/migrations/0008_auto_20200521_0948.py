# Generated by Django 3.0.6 on 2020-05-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdb_app', '0007_film_plot'),
    ]

    operations = [
        migrations.AddField(
            model_name='attore',
            name='e_src',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attore',
            name='tmdb_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='attore',
            name='films',
            field=models.ManyToManyField(null=True, to='mdb_app.Film'),
        ),
        migrations.AlterField(
            model_name='film',
            name='generi',
            field=models.ManyToManyField(blank=True, null=True, to='mdb_app.Genere'),
        ),
    ]
