# Generated by Django 5.0.4 on 2024-08-27 11:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("gestion", "0003_bonentre_code_produit_bonsortie_code_produit"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bonentre",
            name="code_produit",
        ),
    ]
