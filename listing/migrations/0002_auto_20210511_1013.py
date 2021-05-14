# Generated by Django 3.1.7 on 2021-05-11 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20210504_0141'),
        ('console', '0005_console_short_name'),
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='console',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='console.console'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='rent_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='listing',
            name='sell_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='listing',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='game.game'),
        ),
    ]