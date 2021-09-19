# Generated by Django 2.2.5 on 2021-09-19 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20210919_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HouseRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.RoomType'),
        ),
        migrations.AddField(
            model_name='room',
            name='Amenity',
            field=models.ManyToManyField(to='rooms.Amenity'),
        ),
        migrations.AddField(
            model_name='room',
            name='Facility',
            field=models.ManyToManyField(to='rooms.Facility'),
        ),
        migrations.AddField(
            model_name='room',
            name='HouseRule',
            field=models.ManyToManyField(to='rooms.HouseRule'),
        ),
    ]