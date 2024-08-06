# Generated by Django 5.0.6 on 2024-05-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('future_apps', '0003_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='brand',
            field=models.CharField(default='select_shoe', max_length=255),
        ),
    ]
