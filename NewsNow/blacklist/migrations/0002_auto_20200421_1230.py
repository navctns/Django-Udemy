# Generated by Django 2.2.5 on 2020-04-21 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blacklist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blacklist',
            old_name='name',
            new_name='ip',
        ),
    ]
