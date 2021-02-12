# Generated by Django 3.1.6 on 2021-02-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generics', '0005_auto_20210212_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
    ]