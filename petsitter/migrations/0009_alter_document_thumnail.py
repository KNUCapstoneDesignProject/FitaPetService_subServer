# Generated by Django 4.1.1 on 2022-11-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("petsitter", "0008_alter_document_thumnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="thumnail",
            field=models.CharField(max_length=10000),
        ),
    ]
