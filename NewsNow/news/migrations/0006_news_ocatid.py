# Generated by Django 2.2.5 on 2020-03-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ocatid',
            field=models.IntegerField(default=0),
        ),
    ]
