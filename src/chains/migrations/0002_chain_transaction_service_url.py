# Generated by Django 3.2.4 on 2021-06-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chains", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chain",
            name="transaction_service_url",
            field=models.URLField(null=True),
        ),
    ]
