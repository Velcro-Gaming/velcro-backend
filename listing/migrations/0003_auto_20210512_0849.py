# Generated by Django 3.1.7 on 2021-05-12 08:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0005_console_short_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0003_auto_20210504_0141'),
        ('listing', '0002_auto_20210511_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('swapped', 'Swapped'), ('rented', 'Rented'), ('sold', 'Sold')], default='available', max_length=120),
        ),
        migrations.AlterUniqueTogether(
            name='listing',
            unique_together={('owner', 'game', 'console')},
        ),
    ]