# Generated by Django 4.1.7 on 2023-04-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulsearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='app',
            field=models.CharField(default='', max_length=256),
        ),
    ]
