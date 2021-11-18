# Generated by Django 3.2.7 on 2021-11-18 21:03

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
                ('area_center', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('area_boundary', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('area_coords', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
            options={
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='KickBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.area')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.event')),
            ],
            options={
                'db_table': 'kickboards',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('start_area', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('end_area', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('fee', models.PositiveIntegerField()),
                ('kickborad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.kickboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='ParkingZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
                ('parking_center', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('parking_radius', models.DecimalField(decimal_places=10, max_digits=20)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.area')),
            ],
            options={
                'db_table': 'parking_zones',
            },
        ),
        migrations.CreateModel(
            name='ForbiddenArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
                ('forbidden_boundary', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('forbidden_coords', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.area')),
            ],
            options={
                'db_table': 'forbidden_areas',
            },
        ),
    ]