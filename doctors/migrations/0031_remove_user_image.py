# Generated by Django 3.2 on 2021-06-02 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0030_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
