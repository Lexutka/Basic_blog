# Generated by Django 4.0.3 on 2022-04-13 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vostok', '0002_rename_photo_comment_photo1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='photo1',
            new_name='photo',
        ),
    ]
