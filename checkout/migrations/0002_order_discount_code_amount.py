# Generated by Django 3.2.22 on 2023-12-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_code_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
