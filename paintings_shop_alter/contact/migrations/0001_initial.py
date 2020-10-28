# Generated by Django 2.2.5 on 2020-10-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('message', models.TextField(default='-')),
            ],
        ),
    ]
