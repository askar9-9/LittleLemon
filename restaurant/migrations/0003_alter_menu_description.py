# Generated by Django 4.1.3 on 2023-10-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
