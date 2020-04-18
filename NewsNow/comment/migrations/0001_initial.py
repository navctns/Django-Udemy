# Generated by Django 2.2.5 on 2020-04-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('cm', models.TextField()),
                ('news_id', models.IntegerField()),
                ('date', models.CharField(max_length=12)),
                ('time', models.CharField(max_length=10)),
            ],
        ),
    ]
