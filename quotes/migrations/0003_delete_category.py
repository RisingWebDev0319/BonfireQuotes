# Generated by Django 2.2.5 on 2019-11-03 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
