# Generated by Django 4.1.7 on 2023-04-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='default.png', upload_to='thumbnails/'),
        ),
    ]
