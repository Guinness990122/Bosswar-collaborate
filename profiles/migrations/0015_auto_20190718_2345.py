# Generated by Django 2.2.3 on 2019-07-18 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20190718_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='point',
            field=models.PositiveIntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='votes',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
