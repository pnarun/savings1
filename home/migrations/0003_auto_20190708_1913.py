# Generated by Django 2.2.3 on 2019-07-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='contact',
            field=models.CharField(max_length=10, null=True, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='user_register',
            name='firstname',
            field=models.CharField(max_length=10, null=True, verbose_name='firstname'),
        ),
        migrations.AlterField(
            model_name='user_register',
            name='lastname',
            field=models.CharField(max_length=10, null=True, verbose_name='lastname'),
        ),
        migrations.AlterField(
            model_name='user_register',
            name='password',
            field=models.CharField(max_length=16, null=True, verbose_name='password'),
        ),
    ]