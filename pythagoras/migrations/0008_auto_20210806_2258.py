# Generated by Django 3.2.3 on 2021-08-06 15:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythagoras', '0007_auto_20210801_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthdayDayPath',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('key_info', models.CharField(default='', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('meaning', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'CHỈ SỐ NGÀY SINH',
                'verbose_name_plural': 'CHỈ SỐ NGÀY SINH',
            },
        ),
        migrations.CreateModel(
            name='BirthdayMonthPath',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('key_info', models.CharField(default='', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('meaning', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'THÁNG CÁ NHÂN',
                'verbose_name_plural': 'CHỈ SỐ THÁNG CÁ NHÂN',
            },
        ),
        migrations.CreateModel(
            name='BirthdayYearPath',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('key_info', models.CharField(default='', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('meaning', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'NĂM CÁ NHÂN',
                'verbose_name_plural': 'CHỈ SỐ NĂM CÁ NHÂN',
            },
        ),
        migrations.CreateModel(
            name='ChallengePath',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('key_info', models.CharField(default='', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('meaning', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'CHỈ SỐ THÁCH THỨC',
                'verbose_name_plural': 'CHỈ SỐ THÁCH THỨC',
            },
        ),
        migrations.CreateModel(
            name='CyclePath',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('key_info', models.CharField(default='', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('meaning', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'CHỈ SỐ CHU KỲ',
                'verbose_name_plural': 'CHỈ SỐ CHU KỲ LỚN',
            },
        ),
        migrations.CreateModel(
            name='MissingPath',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('key_info', models.CharField(default='', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('meaning', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'CHỈ SỐ THIẾU',
                'verbose_name_plural': 'CHỈ SỐ RÈN LUYỆN',
            },
        ),
        migrations.CreateModel(
            name='PassionPath',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('key_info', models.CharField(default='', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('meaning', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'CHỈ SỐ ĐAM MÊ',
                'verbose_name_plural': 'CHỈ SỐ ĐAM MÊ',
            },
        ),
        migrations.CreateModel(
            name='PyramidPath',
            fields=[
                ('model_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('key_info', models.CharField(default='', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('meaning', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'CHỈ SỐ CHẶNG',
                'verbose_name_plural': 'CHỈ SỐ CHẶNG',
            },
        ),
        migrations.RenameModel(
            old_name='ExpressionPath',
            new_name='AttitudePath',
        ),
        migrations.AlterModelOptions(
            name='attitudepath',
            options={'verbose_name': 'SỐ THÁI ĐỘ', 'verbose_name_plural': 'CHỈ SỐ THÁI ĐỘ'},
        ),
        migrations.AlterModelOptions(
            name='hearthdesire',
            options={'verbose_name': 'SỐ ĐỘNG LỰC', 'verbose_name_plural': 'CHỈ SỐ ĐỘNG LỰC'},
        ),
        migrations.AlterModelOptions(
            name='legacypath',
            options={'verbose_name': 'HỌ HIỆN TẠI', 'verbose_name_plural': 'CHỈ SỐ HỌ HIỆN TẠI'},
        ),
        migrations.AlterModelOptions(
            name='lifepath',
            options={'verbose_name': 'SỐ ĐƯỜNG ĐỜI', 'verbose_name_plural': 'CHỈ SỐ ĐƯỜNG ĐỜI'},
        ),
        migrations.AlterModelOptions(
            name='personality',
            options={'verbose_name': 'TÍNH CÁCH', 'verbose_name_plural': 'CHỈ SỐ TÍNH CÁCH'},
        ),
        migrations.AlterModelOptions(
            name='powerpath',
            options={'verbose_name': 'THÀNH TỰU', 'verbose_name_plural': 'CHỈ SỐ THÀNH TỰU'},
        ),
    ]