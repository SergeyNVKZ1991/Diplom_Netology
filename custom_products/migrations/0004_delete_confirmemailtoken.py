# Generated by Django 4.2.2 on 2023-08-17 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_products', '0003_alter_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConfirmEmailToken',
        ),
    ]
