# Generated by Django 4.0.2 on 2022-02-28 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_index_together'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
    ]