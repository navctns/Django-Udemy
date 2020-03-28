# Generated by Django 2.2.5 on 2020-03-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_txt', models.TextField()),
                ('body_txt', models.TextField()),
                ('date', models.CharField(max_length=12)),
                ('writer', models.CharField(max_length=50)),
                ('set_name', models.TextField(default='-')),
            ],
        ),
    ]