# Generated by Django 3.0.2 on 2020-03-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20200330_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_num',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='postcode',
            name='postcode',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
