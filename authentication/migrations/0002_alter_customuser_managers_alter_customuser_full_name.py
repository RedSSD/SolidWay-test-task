# Generated by Django 5.0.6 on 2024-05-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[],
        ),
        migrations.AlterField(
            model_name="customuser",
            name="full_name",
            field=models.CharField(max_length=255),
        ),
    ]