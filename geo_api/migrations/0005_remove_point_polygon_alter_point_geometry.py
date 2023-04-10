# Generated by Django 4.1.7 on 2023-04-07 07:41

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_api', '0004_alter_linestring_geometry_alter_point_geometry_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='polygon',
        ),
        migrations.AlterField(
            model_name='point',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Точка'),
        ),
    ]
