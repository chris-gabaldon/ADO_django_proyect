# Generated by Django 4.1 on 2024-11-13 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("experimento", "0012_remove_experimentsession_current_d1_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trial",
            name="correct",
        ),
    ]
