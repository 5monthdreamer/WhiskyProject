# Generated by Django 3.2.9 on 2022-05-10 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0009_alter_uploadimagemodel_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimagemodel',
            name='nickname',
        ),
    ]
