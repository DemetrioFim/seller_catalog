# Generated by Django 5.1.1 on 2024-09-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_itemcesta_preco_unitario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemcesta",
            name="preco_unitario",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0.0, max_digits=10, null=True
            ),
        ),
    ]
