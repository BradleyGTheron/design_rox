# Generated by Django 2.2.5 on 2020-03-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0005_auto_20200327_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='print',
            name='home_page',
            field=models.BooleanField(default=False),
        ),
    ]