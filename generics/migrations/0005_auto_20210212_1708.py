# Generated by Django 3.1.6 on 2021-02-12 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generics', '0004_auto_20210212_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='replies',
            new_name='reply_to',
        ),
    ]