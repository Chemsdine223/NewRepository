# Generated by Django 4.1.7 on 2023-05-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_bankclient_account_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="bankclient",
            name="image",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
