# Generated by Django 4.0.2 on 2022-02-28 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_product_category'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
