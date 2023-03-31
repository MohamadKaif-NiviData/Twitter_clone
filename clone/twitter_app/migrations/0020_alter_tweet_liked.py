# Generated by Django 3.2.16 on 2023-03-30 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0019_tweet_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='liked',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
