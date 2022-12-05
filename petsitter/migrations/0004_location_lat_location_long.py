# Generated by Django 4.1.1 on 2022-11-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("petsitter", "0003_document_filesize"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="lat",
            field=models.FloatField(default=37.541),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="location",
            name="long",
            field=models.FloatField(default=126.986),
            preserve_default=False,
        ),
    ]