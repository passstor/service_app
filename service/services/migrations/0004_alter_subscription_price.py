# Generated by Django 3.2.16 on 2023-04-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_rename_discount_percent_subscription_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]