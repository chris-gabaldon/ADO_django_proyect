# Generated by Django 5.1.2 on 2024-11-05 03:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experimento", "0003_alter_trial_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="trial",
            name="participant_id",
            field=models.CharField(default=999, max_length=100),
            preserve_default=False,
        ),
    ]
