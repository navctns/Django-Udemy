# Generated by Django 2.2.5 on 2020-10-27 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0)),
                ('categ_id', models.IntegerField(default=0)),
                ('categ_name', models.CharField(default='-', max_length=30)),
                ('picname', models.TextField(default='-', max_length=12)),
                ('picurl', models.TextField(default='-')),
                ('artist', models.TextField(default='-', max_length=100)),
                ('description', models.TextField(default='-', max_length=200)),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
    ]