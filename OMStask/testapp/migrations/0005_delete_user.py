# Generated by Django 2.0.5 on 2020-05-12 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]