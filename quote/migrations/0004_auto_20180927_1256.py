# Generated by Django 2.1 on 2018-09-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_auto_20180927_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_slug',
            field=models.SlugField(max_length=100),
        ),
    ]