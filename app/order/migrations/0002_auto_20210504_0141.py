# Generated by Django 3.1.7 on 2021-05-04 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='order',
            name='game',
        ),
        migrations.RemoveField(
            model_name='order',
            name='games',
        ),
        migrations.AddField(
            model_name='order',
            name='listing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='listing.listing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='offered_listings',
            field=models.ManyToManyField(related_name='orders', to='listing.Listing'),
        ),
    ]