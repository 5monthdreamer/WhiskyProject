# Generated by Django 3.2.9 on 2022-09-12 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0006_auto_20220912_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimagemodel',
            name='followuser',
        ),
        migrations.CreateModel(
            name='UploadNoteFollowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_follow', models.BooleanField(default=False)),
                ('UploadImagekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.tastingnotemodel')),
                ('follower', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadImageFollowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_follow', models.BooleanField(default=False)),
                ('UploadImagekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.uploadimagemodel')),
                ('follower', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
