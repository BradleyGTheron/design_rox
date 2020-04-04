# Generated by Django 2.2.5 on 2020-03-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0004_auto_20200320_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='print',
            name='length',
        ),
        migrations.RemoveField(
            model_name='print',
            name='width',
        ),
        migrations.AddField(
            model_name='print',
            name='size',
            field=models.CharField(choices=[('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5')], default='A4', max_length=3, verbose_name='Print Size'),
        ),
    ]