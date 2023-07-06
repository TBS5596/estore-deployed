# Generated by Django 4.1.3 on 2023-07-06 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
        ('cart', '0002_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='item.item'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]