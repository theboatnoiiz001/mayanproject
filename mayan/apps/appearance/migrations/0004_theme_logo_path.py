# Generated by Django 2.2.24 on 2022-03-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0003_auto_20210823_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='logo_path',
            field=models.TextField(blank=True, help_text='This is path logo.', verbose_name='Logo_path'),
        ),
    ]
