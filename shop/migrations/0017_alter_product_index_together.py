# Generated by Django 4.0.2 on 2022-02-28 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_product_index_together'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
    ]
