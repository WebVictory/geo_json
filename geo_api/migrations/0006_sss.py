# Generated by Django 4.1.7 on 2023-04-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_api', '0005_remove_point_polygon_alter_point_geometry'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
        ),
    ]
