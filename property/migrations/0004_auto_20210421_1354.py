# Generated by Django 2.2.20 on 2021-04-21 10:54

from django.db import migrations


def update_field_new_building(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    new_building_flats = Flat.objects.filter(construction_year__gte="2015")
    new_building_flats.update(new_building=True)
    old_building_flats = Flat.objects.filter(construction_year__lte="2014")
    old_building_flats.update(new_building=False)


def move_backward(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    flats = Flat.objects.all()
    flats.update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0003_flat_new_building"),
    ]

    operations = [
        migrations.RunPython(update_field_new_building, move_backward),
    ]
