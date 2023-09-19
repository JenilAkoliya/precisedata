# Generated by Django 4.2.1 on 2023-06-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preciseweb', '0002_getstarted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getstarted',
            name='address',
        ),
        migrations.RemoveField(
            model_name='getstarted',
            name='country',
        ),
        migrations.AddField(
            model_name='getstarted',
            name='message',
            field=models.TextField(default='', max_length=1100),
        ),
    ]
