# Generated by Django 2.2.5 on 2021-09-22 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20210919_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='Amenity',
            new_name='amenities',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='Facility',
            new_name='facilities',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='HouseRule',
            new_name='house_rules',
        ),
    ]
