# Generated by Django 4.1.7 on 2024-06-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('future_apps', '0024_alter_post_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
