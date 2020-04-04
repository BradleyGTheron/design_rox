# Generated by Django 2.2.5 on 2020-03-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0003_auto_20200317_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='Discount (%)'),
        ),
        migrations.AlterField(
            model_name='print',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Selling Price (R)'),
        ),
    ]
