# Generated by Django 2.2.5 on 2019-11-15 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0026_auto_20191114_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='feature',
        ),
        migrations.AddField(
            model_name='post',
            name='feature_qotd',
            field=models.BooleanField(default=False, verbose_name='Featured QOTD'),
        ),
    ]
