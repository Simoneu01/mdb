# Generated by Django 3.0.6 on 2020-05-23 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdb_app', '0010_libro_plot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='scrittore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mdb_app.Scrittore'),
        ),
    ]