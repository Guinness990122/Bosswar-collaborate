# Generated by Django 2.2.3 on 2019-07-18 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20190718_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='point',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='votes',
        ),
    ]