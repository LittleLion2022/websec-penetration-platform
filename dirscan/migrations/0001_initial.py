# Generated by Django 4.1.7 on 2023-04-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dirs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('httpcode', models.IntegerField()),
                ('service', models.CharField(default='unknown', max_length=30)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
