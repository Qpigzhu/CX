# Generated by Django 2.0 on 2018-06-13 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='postr_url_big',
            new_name='poster_url_big',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='postr_url_me',
            new_name='poster_url_me',
        ),
    ]