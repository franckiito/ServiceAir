# Generated by Django 2.1.2 on 2019-06-12 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.TipoServicio'),
        ),
        migrations.AddField(
            model_name='agendamiento',
            name='tecnico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agendamiento',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.TipoServicio'),
        ),
    ]
