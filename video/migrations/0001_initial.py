# Generated by Django 3.1.6 on 2021-02-07 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('total_likes', models.PositiveIntegerField(db_index=True, default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos_created', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('users_likes', models.ManyToManyField(blank=True, related_name='videos_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
