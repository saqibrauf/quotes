# Generated by Django 2.1 on 2018-09-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0002_quote_quote_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('tag_slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='author_slug',
            field=models.SlugField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_slug',
            field=models.SlugField(editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(blank=True, to='quote.Tag'),
        ),
    ]