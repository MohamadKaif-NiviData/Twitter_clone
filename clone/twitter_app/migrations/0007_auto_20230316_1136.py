# Generated by Django 3.2.16 on 2023-03-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0006_auto_20230316_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(default='user.png', upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Img_upload',
        ),
    ]