# Generated by Django 4.2.5 on 2023-09-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sencuisineByfa", "0002_userprofile_bio_userprofile_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredient",
            name="quantite",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=None, max_digits=10, null=True
            ),
        ),
    ]
