# Generated by Django 3.1.6 on 2021-02-12 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generics', '0002_auto_20210212_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies_created', to='generics.comment'),
        ),
    ]