# Generated by Django 4.2.7 on 2023-11-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_remove_transaction_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account_number',
            field=models.BigIntegerField(),
        ),
    ]
