# Generated by Django 5.1.2 on 2024-11-20 00:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experimento", "0014_attentioncheck"),
    ]

    operations = [
        migrations.AddField(
            model_name="experimentsession",
            name="correct_responses",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="experimentsession",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.DeleteModel(
            name="AttentionCheck",
        ),
    ]
