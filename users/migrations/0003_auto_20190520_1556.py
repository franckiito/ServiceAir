# Generated by Django 2.2.1 on 2019-05-20 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190520_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='colegio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Colegio'),
        ),
    ]