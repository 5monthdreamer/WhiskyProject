# Generated by Django 3.2.9 on 2022-08-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_auto_20220818_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tastingnotemodel',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
