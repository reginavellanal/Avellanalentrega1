# Generated by Django 4.1.4 on 2023-01-29 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_delete_categorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='distance',
        ),
    ]
