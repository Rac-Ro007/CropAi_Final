# Generated by Django 2.1.5 on 2019-03-02 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0005_buyer_demand_farmer_crops'),
    ]

    operations = [
        migrations.DeleteModel(
            name='buyer_demand',
        ),
        migrations.DeleteModel(
            name='farmer_crops',
        ),
    ]