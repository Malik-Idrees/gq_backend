# Generated by Django 4.0.3 on 2022-05-20 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_video_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
