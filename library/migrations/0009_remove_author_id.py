# Generated by Django 5.0.3 on 2024-03-10 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20240310_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
    ]