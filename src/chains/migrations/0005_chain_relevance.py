# Generated by Django 3.2.4 on 2021-06-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chains", "0004_auto_20210622_1353"),
    ]

    operations = [
        migrations.AddField(
            model_name="chain",
            name="relevance",
            field=models.SmallIntegerField(default=100),
        ),
    ]
