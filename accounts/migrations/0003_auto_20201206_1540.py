# Generated by Django 3.1.2 on 2020-12-06 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201206_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='appusers',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_owner',
        ),
    ]