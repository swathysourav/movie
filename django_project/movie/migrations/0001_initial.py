# Generated by Django 4.2.10 on 2024-02-25 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=250)),
                ('movie_description', models.TextField()),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('movie_image', models.ImageField(blank=True, null=True, upload_to='gallery')),
                ('actors', models.CharField(max_length=250)),
                ('youtube', models.CharField(max_length=250)),
                ('movie_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=250)),
                ('rating', models.FloatField()),
                ('movie_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.post')),
            ],
        ),
    ]
