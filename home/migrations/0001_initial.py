# Generated by Django 2.2.3 on 2019-07-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='savings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('money_to_be_saved', models.CharField(max_length=6, verbose_name='Money to be Saved')),
                ('deadline', models.CharField(max_length=3, verbose_name='Target Days')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
