# Generated by Django 4.2 on 2024-09-29 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Print_Square', '0002_remove_print_square_inquiry_inquiryid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='print_square_order',
            name='Cash',
        ),
    ]