# Generated by Django 4.1.7 on 2024-05-31 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('future_apps', '0018_alter_post_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brand',
            field=models.CharField(default='Nike', max_length=255),
        ),
    ]