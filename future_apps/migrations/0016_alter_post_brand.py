# Generated by Django 4.1.7 on 2024-05-31 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('future_apps', '0015_alter_post_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brand',
            field=models.CharField(default='select_shoe', max_length=255),
        ),
    ]
