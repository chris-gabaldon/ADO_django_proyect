# Generated by Django 5.1.2 on 2024-11-02 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExperimentSession",
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
                ("participant_id", models.CharField(max_length=100)),
                ("start_time", models.DateTimeField(auto_now_add=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Block",
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
                ("block_number", models.IntegerField()),
                ("performance", models.FloatField(blank=True, null=True)),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experimento.experimentsession",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trial",
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
                ("trial_id", models.IntegerField()),  # Add trial_id here if needed
                ("trial_number", models.IntegerField()),
                ("stimulus", models.CharField(max_length=10)),
                ("response", models.CharField(blank=True, max_length=10, null=True)),
                ("correct", models.BooleanField(blank=True, null=True)),
                ("reaction_time", models.FloatField(blank=True, null=True)),
                (
                    "block",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experimento.block",
                    ),
                ),
            ],
        ),
    ]