# Generated by Django 2.2.5 on 2020-03-24 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subcat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cat',
            new_name='SubCat',
        ),
    ]
