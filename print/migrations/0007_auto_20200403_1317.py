# Generated by Django 2.2.5 on 2020-04-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0006_print_home_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='print',
            name='image_tn',
            field=models.ImageField(blank=True, upload_to='prints/', verbose_name='Thumbnail Image'),
        ),
        migrations.AlterField(
            model_name='print',
            name='image',
            field=models.ImageField(blank=True, upload_to='prints/', verbose_name='Main Image'),
        ),
    ]
