# Generated by Django 4.1.2 on 2022-10-27 14:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_updated_at_alter_post_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "average_score",
                    models.PositiveSmallIntegerField(
                        validators=[django.core.validators.MaxValueValidator(5)]
                    ),
                ),
            ],
        ),
    ]
