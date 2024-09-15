# Generated by Django 5.0.4 on 2024-08-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code_produit", models.CharField(max_length=50)),
                ("designation", models.CharField(max_length=50)),
                ("date_fabrication", models.DateField()),
                ("unite", models.IntegerField(max_length=50)),
                ("quantite_utilisee", models.IntegerField()),
                ("quantite_stock", models.IntegerField()),
            ],
        ),
    ]
