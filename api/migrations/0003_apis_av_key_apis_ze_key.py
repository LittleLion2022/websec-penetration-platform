# Generated by Django 4.1.7 on 2023-04-20 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_apis_vt_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='apis',
            name='av_key',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='apis',
            name='ze_key',
            field=models.CharField(default='', max_length=256),
        ),
    ]
