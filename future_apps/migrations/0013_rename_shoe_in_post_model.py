# Generated by Django 5.0.6 on 2024-05-29 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('future_apps', '0012_post_colaboration_post_color_scheme_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='shoe_in',
            new_name='model',
        ),
    ]