# Generated by Django 3.2.9 on 2022-10-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0016_auto_20221002_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tastingnotemodel',
            name='long_review',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
