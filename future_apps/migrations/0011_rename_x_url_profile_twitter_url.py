# Generated by Django 5.0.6 on 2024-05-29 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('future_apps', '0010_profile_instagram_url_profile_linkedin_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='x_url',
            new_name='twitter_url',
        ),
    ]