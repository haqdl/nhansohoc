# Generated by Django 3.2.3 on 2021-08-01 14:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythagoras', '0006_alter_lifepath_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activepath',
            options={'verbose_name': 'TÊN HIỆN TẠI', 'verbose_name_plural': 'CHỈ SỐ TÊN HIỆN TẠI'},
        ),
        migrations.AlterModelOptions(
            name='destinypath',
            options={'verbose_name': 'SỨ MỆNH', 'verbose_name_plural': 'CHỈ SỐ SỨ MỆNH'},
        ),
        migrations.AlterModelOptions(
            name='expressionpath',
            options={'verbose_name': 'Expression ', 'verbose_name_plural': 'Expression Path'},
        ),
        migrations.AlterModelOptions(
            name='hearthdesire',
            options={'verbose_name': 'LINH HỒN', 'verbose_name_plural': 'CHỈ SỐ LINH HỒN'},
        ),
        migrations.AlterModelOptions(
            name='legacypath',
            options={'verbose_name': 'Legac', 'verbose_name_plural': 'Legacy Path'},
        ),
        migrations.AlterModelOptions(
            name='lifepath',
            options={'verbose_name': 'SỐ CHỦ ĐẠO', 'verbose_name_plural': 'CHỈ SỐ CHỦ ĐẠO'},
        ),
        migrations.AlterModelOptions(
            name='personality',
            options={'verbose_name': 'NHÂN CÁCH', 'verbose_name_plural': 'CHỈ SỐ NHÂN CÁCH'},
        ),
        migrations.AlterModelOptions(
            name='powerpath',
            options={'verbose_name': 'SỐ TRƯỞNG THÀNH', 'verbose_name_plural': 'CHỈ SỐ TRƯỞNG THÀNH'},
        ),
        migrations.RenameField(
            model_name='activepath',
            old_name='active_number',
            new_name='model_number',
        ),
        migrations.RenameField(
            model_name='destinypath',
            old_name='destiny_path_number',
            new_name='model_number',
        ),
        migrations.RenameField(
            model_name='expressionpath',
            old_name='expression_number',
            new_name='model_number',
        ),
        migrations.RenameField(
            model_name='hearthdesire',
            old_name='hearth_desire_number',
            new_name='model_number',
        ),
        migrations.RenameField(
            model_name='legacypath',
            old_name='legacy_number',
            new_name='model_number',
        ),
        migrations.RenameField(
            model_name='lifepath',
            old_name='life_path_number',
            new_name='model_number',
        ),
        migrations.RenameField(
            model_name='personality',
            old_name='personality_number',
            new_name='model_number',
        ),
        migrations.RenameField(
            model_name='powerpath',
            old_name='power_number',
            new_name='model_number',
        ),
        migrations.AddField(
            model_name='activepath',
            name='key_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='destinypath',
            name='key_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='expressionpath',
            name='key_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hearthdesire',
            name='key_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='legacypath',
            name='key_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lifepath',
            name='key_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='personality',
            name='key_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='powerpath',
            name='key_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='activepath',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='activepath',
            name='meaning',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='destinypath',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='destinypath',
            name='meaning',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='expressionpath',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='expressionpath',
            name='meaning',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='hearthdesire',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='hearthdesire',
            name='meaning',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='legacypath',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='legacypath',
            name='meaning',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lifepath',
            name='meaning',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='personality',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='personality',
            name='meaning',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='powerpath',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='powerpath',
            name='meaning',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
