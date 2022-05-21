# Generated by Django 4.0.3 on 2022-05-20 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='category',
            new_name='goalToAchieve',
        ),
        migrations.AddField(
            model_name='course',
            name='dailyTime',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='expertiseLevel',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='job',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
