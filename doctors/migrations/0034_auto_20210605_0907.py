# Generated by Django 3.2 on 2021-06-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0033_instance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='mainname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='mainprob',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
