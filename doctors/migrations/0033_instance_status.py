# Generated by Django 3.2 on 2021-06-04 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0032_user_encryptid'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
