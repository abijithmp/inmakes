# Generated by Django 4.2.1 on 2023-05-10 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("details", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="person",
            old_name="date",
            new_name="dob",
        ),
    ]
