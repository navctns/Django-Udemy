# Generated by Django 2.2.5 on 2020-10-28 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
