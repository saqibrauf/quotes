# Generated by Django 2.1 on 2018-09-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0005_auto_20180927_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_slug',
            field=models.SlugField(blank=True, editable=False, max_length=100),
        ),
    ]
