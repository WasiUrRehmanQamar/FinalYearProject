# Generated by Django 3.2 on 2023-04-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name_plural': 'Content'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name_plural': 'Department'},
        ),
        migrations.AlterModelOptions(
            name='eventcategory',
            options={'verbose_name_plural': 'EventCategory'},
        ),
        migrations.AlterModelOptions(
            name='eventcategorycontent',
            options={'verbose_name_plural': 'EventCategoryContent'},
        ),
        migrations.AlterModelOptions(
            name='eventcategorycontentwebsite',
            options={'verbose_name_plural': 'EventCategoryContentWebsite'},
        ),
        migrations.AlterModelOptions(
            name='masteruser',
            options={'verbose_name_plural': 'MasterUser'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name_plural': 'Menu'},
        ),
        migrations.AlterModelOptions(
            name='newsupdates',
            options={'verbose_name_plural': 'NewsUpdates'},
        ),
        migrations.AlterModelOptions(
            name='newsupdateswebsite',
            options={'verbose_name_plural': 'NewsUpdatesWebsite'},
        ),
        migrations.AlterModelOptions(
            name='rolegroup',
            options={'verbose_name_plural': 'RoleGroup'},
        ),
        migrations.AlterModelOptions(
            name='rolemenu',
            options={'verbose_name_plural': 'RoleMenu'},
        ),
        migrations.AlterModelOptions(
            name='society',
            options={'verbose_name_plural': 'Society'},
        ),
        migrations.AlterModelOptions(
            name='usergroup',
            options={'verbose_name_plural': 'UserGroup'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name_plural': 'UserRole'},
        ),
        migrations.AlterModelOptions(
            name='website',
            options={'verbose_name_plural': 'Website'},
        ),
        migrations.AlterField(
            model_name='campus',
            name='ModifiedDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]