# Generated by Django 4.1 on 2024-11-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experimento", "0006_trial_d1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trial",
            name="d1",
            field=models.IntegerField(default=1),
        ),
    ]
