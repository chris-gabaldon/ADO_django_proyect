# Generated by Django 5.1.2 on 2024-11-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experimento", "0015_experimentsession_correct_responses_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="trial",
            name="participant_id_random",
            field=models.CharField(default="default_value", max_length=100),
        ),
    ]
