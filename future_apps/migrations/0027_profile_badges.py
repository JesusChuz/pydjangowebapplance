# Generated by Django 3.2.18 on 2024-07-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('future_apps', '0026_alter_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='badges',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
