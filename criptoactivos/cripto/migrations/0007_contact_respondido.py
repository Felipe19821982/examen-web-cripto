# Generated by Django 5.0.6 on 2024-07-19 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cripto', '0006_compra_user_alter_compra_crypto_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='respondido',
            field=models.BooleanField(default=False),
        ),
    ]
