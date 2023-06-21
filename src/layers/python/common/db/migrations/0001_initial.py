# Generated by Django 4.2.2 on 2023-06-21 11:49
from typing import Any, List

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: List[Any] = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("customerId", models.CharField(max_length=100)),
            ],
        ),
    ]
