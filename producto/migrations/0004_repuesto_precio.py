# Generated by Django 2.1.5 on 2019-06-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_auto_20190620_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='precio',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]