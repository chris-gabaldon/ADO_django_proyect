# Generated by Django 5.1.2 on 2024-11-19 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experimento", "0013_remove_trial_correct"),
    ]

    operations = [
        migrations.CreateModel(
            name="AttentionCheck",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("trial_number", models.IntegerField()),
                ("question", models.TextField()),
                ("correct_answer", models.CharField(max_length=255)),
                (
                    "user_answer",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("is_correct", models.BooleanField(default=False)),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experimento.experimentsession",
                    ),
                ),
            ],
        ),
    ]