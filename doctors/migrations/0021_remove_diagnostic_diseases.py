# Generated by Django 3.2 on 2021-05-30 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0020_disease'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostic',
            name='diseases',
        ),
    ]
