# Generated by Django 3.2.22 on 2023-12-03 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_tip_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tip_percentage',
        ),
    ]
