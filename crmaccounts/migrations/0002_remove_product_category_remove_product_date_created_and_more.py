# Generated by Django 5.0.7 on 2024-08-01 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmaccounts', '0001_initial'),
        ('item', '0004_city_remove_item_location_item_city'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ManyToManyField(related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
