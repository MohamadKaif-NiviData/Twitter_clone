# Generated by Django 3.2.16 on 2023-03-31 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0023_like_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='retweet',
            field=models.ManyToManyField(blank=True, default=None, related_name='retweet_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tweet', to='twitter_app.tweet'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ReTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('ReTweet', 'Tweet'), ('Retweeted', 'Retweeted')], default='Like', max_length=20)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_retweet', to='twitter_app.tweet')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_retweet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]