# Generated by Django 4.2.1 on 2023-06-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preciseweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Getstarted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('workemail', models.CharField(max_length=30)),
                ('phone', models.TextField(max_length=20)),
                ('country', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]
