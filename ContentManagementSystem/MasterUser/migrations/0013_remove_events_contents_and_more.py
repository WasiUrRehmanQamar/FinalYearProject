# Generated by Django 4.1.7 on 2023-06-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterUser', '0012_campusgroups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='studentnoticeboard',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='trends',
            name='contents',
        ),
        migrations.AddField(
            model_name='events',
            name='Image',
            field=models.ImageField(default='', upload_to='upload/events/'),
        ),
        migrations.AddField(
            model_name='studentnoticeboard',
            name='Image',
            field=models.ImageField(default='', upload_to='upload/noticeboard/'),
        ),
        migrations.AddField(
            model_name='trends',
            name='Image',
            field=models.ImageField(default='', upload_to='upload/trends/'),
        ),
    ]