# Generated by Django 2.1.7 on 2019-04-11 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20190411_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
    ]
