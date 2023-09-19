# Generated by Django 4.2.1 on 2023-06-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('subject', models.TextField(max_length=200)),
                ('message', models.TextField(max_length=2000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]
