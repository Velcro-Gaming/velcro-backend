# Generated by Django 3.1.7 on 2021-05-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userverification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userverification',
            name='is_checked',
        ),
        migrations.RemoveField(
            model_name='userverification',
            name='is_valid',
        ),
        migrations.AddField(
            model_name='userverification',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('unverified', 'unverified')], default='unverified', max_length=60),
        ),
    ]
