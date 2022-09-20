# Generated by Django 3.2.9 on 2022-08-18 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_rename_star_rating_tastingnotemodel_drumtong_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tastingnotemodel',
            name='UploadImagekey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.uploadimagemodel'),
        ),
        migrations.AlterField(
            model_name='tastingnotemodel',
            name='name',
            field=models.CharField(error_messages={'required': 'Input data please'}, max_length=20),
        ),
    ]
