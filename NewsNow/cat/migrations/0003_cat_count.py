# Generated by Django 2.2.5 on 2020-03-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0002_cat_set_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
