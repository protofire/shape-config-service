# Generated by Django 3.2.5 on 2021-07-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chains", "0013_rename_url_uri"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chain",
            name="transaction_service_uri",
            field=models.URLField(),
        ),
    ]
