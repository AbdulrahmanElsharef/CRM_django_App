# Generated by Django 4.2 on 2024-10-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etbaly_Shokran', '0003_remove_etbaly_shokran_order_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etbaly_shokran_orderdetail',
            name='Item_Name',
            field=models.TextField(max_length=250, verbose_name='Item_Name'),
        ),
    ]
