# Generated by Django 2.2.5 on 2020-04-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/', verbose_name='Gallery Image')),
                ('image_tn', models.ImageField(upload_to='photos/', verbose_name='Thumbnail Image')),
                ('title', models.CharField(max_length=50, verbose_name='Print Title')),
                ('enabled', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Gallery Photo',
                'verbose_name_plural': 'Gallery Photos',
            },
        ),
    ]
