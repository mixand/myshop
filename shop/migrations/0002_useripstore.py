# Generated by Django 4.0.2 on 2022-02-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIpStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userip', models.CharField(max_length=200)),
                ('countryname', models.CharField(max_length=200)),
                ('regionname', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
            ],
        ),
    ]
