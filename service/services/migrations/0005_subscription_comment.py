# Generated by Django 3.2.16 on 2023-04-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_subscription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='comment',
            field=models.CharField(default='', max_length=100),
        ),
    ]
