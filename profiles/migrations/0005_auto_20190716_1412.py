# Generated by Django 2.2.3 on 2019-07-16 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20190716_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phonenumber',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_phonenumber', message='01012345678 형식으로 입력하세요.', regex='010-[1-9]-\\d{6,7}')]),
        ),
    ]