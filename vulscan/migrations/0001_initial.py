# Generated by Django 4.1.7 on 2023-05-12 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vuls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=30)),
                ('vul', models.CharField(max_length=30)),
                ('vul_id', models.CharField(max_length=30)),
                ('grade', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
