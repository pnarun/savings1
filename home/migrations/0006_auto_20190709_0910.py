# Generated by Django 2.2.3 on 2019-07-09 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190708_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savings',
            name='deadline',
            field=models.CharField(max_length=3, verbose_name='deadline'),
        ),
        migrations.AlterField(
            model_name='savings',
            name='money_to_be_saved',
            field=models.CharField(max_length=6, verbose_name='MoneytobeSaved'),
        ),
    ]