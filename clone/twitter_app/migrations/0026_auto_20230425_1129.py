# Generated by Django 3.2.16 on 2023-04-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0025_alter_retweet_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retweet',
            name='value',
            field=models.CharField(choices=[('ReTweet', 'ReTweet'), ('Remove', 'Remove')], default='ReTweet', max_length=20),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='img',
            field=models.ImageField(blank=True, default='None', null=True, upload_to=''),
        ),
    ]