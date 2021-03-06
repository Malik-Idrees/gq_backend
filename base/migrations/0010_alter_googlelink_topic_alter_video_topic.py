# Generated by Django 4.0.3 on 2022-05-22 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_googlelink_title_alter_googlelink_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlelink',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='base.topic'),
        ),
        migrations.AlterField(
            model_name='video',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.topic'),
        ),
    ]
