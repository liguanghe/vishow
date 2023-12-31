# Generated by Django 4.2.3 on 2023-07-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vishow', '0004_stock_date_stock_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='buy_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='sell_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
