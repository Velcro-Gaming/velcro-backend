# Generated by Django 3.1.7 on 2021-05-04 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userconsole',
            old_name='created_at',
            new_name='added_on',
        ),
        migrations.RemoveField(
            model_name='userconsole',
            name='updated_at',
        ),
    ]
