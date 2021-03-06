# Generated by Django 3.1.5 on 2021-07-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythagoras', '0003_auto_20210628_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpressionPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression_number', models.IntegerField(unique=True)),
                ('meaning', models.TextField(blank=True)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
    ]
