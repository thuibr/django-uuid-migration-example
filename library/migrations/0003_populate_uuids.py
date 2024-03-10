# Generated by Django 5.0.3 on 2024-03-10 12:24

import uuid
from django.db import migrations

def populate_uuids(apps, schema_editor):
    Author = apps.get_model("library", "Author")
    for row in Author.objects.all():
        row.uuid = uuid.uui4()
        row.save(update_fields=["uuid"])


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_author_uuid'),
    ]

    operations = [
            migrations.RunPython(populate_uuids),
    ]
