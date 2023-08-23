# Generated by Django 4.2.4 on 2023-08-22 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="sensor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sensor",
                to="measurement.sensor",
            ),
        ),
    ]