# Generated by Django 5.0.4 on 2024-07-08 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_item_address_item_barangay_item_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='height',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='postal',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
