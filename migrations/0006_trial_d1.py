# Generated by Django 4.1 on 2024-11-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experimento", "0005_experimentsession_last_response"),
    ]

    operations = [
        migrations.AddField(
            model_name="trial",
            name="d1",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]