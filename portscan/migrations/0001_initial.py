# Generated by Django 4.1.7 on 2023-03-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('ip', models.GenericIPAddressField()),
                ('portid', models.IntegerField()),
                ('service', models.CharField(default='unknown', max_length=30)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]