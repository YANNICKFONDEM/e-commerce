# Generated by Django 4.2.6 on 2024-05-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.CharField(default=False, max_length=80),
        ),
    ]
