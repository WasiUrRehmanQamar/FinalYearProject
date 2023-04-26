# Generated by Django 3.2 on 2023-04-07 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20230407_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='CampusAddress',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='campus',
            name='CampusEmail',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='campus',
            name='CampusPhone',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.", regex='^\\+?\\d{11,13}$')]),
        ),
        migrations.AlterField(
            model_name='campus',
            name='ModifiedBy',
            field=models.CharField(max_length=200),
        ),
    ]