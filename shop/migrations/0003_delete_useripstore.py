# Generated by Django 4.0.2 on 2022-02-21 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_useripstore'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserIpStore',
        ),
    ]
