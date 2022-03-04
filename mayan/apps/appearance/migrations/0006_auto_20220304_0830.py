# Generated by Django 2.2.24 on 2022-03-04 08:30

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0005_auto_20220304_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='background_color_header',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background header.', verbose_name='Color background header'),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_color_header_panel',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background header panel.', verbose_name='Color background header panel'),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_color_menu',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background menu.', verbose_name='Color background menu'),
        ),
        migrations.AddField(
            model_name='theme',
            name='color_font_header',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color font header.', verbose_name='Color font header'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='font',
            field=models.CharField(choices=[('Kanit', 'Kanit font'), ('Roboto', 'Roboto font'), ('Prompt', 'Prompt font')], max_length=100, verbose_name='Font'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='logo_img_path',
            field=models.CharField(blank=True, help_text='This is image path logo.', max_length=100, verbose_name='Logo_image_path'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='logo_text',
            field=models.CharField(blank=True, help_text='This is logo text.', max_length=100, verbose_name='Logo_text'),
        ),
    ]