# Generated by Django 2.2.5 on 2020-11-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndivPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picurl', models.TextField(default='-')),
                ('post_desc', models.TextField(default='-')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(),
        ),
    ]
