# Generated by Django 3.2.16 on 2023-03-13 07:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter_app', '0002_auto_20230310_0729'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fllow',
            new_name='Follow',
        ),
    ]
