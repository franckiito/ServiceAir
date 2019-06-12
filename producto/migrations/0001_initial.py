# Generated by Django 2.1.2 on 2019-06-12 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
                ('direccion', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=50)),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
                ('modelo', models.CharField(blank=True, max_length=50)),
                ('capacidad', models.IntegerField(blank=True)),
                ('caudal', models.CharField(blank=True, max_length=50)),
                ('voltaje', models.IntegerField(blank=True)),
                ('consumo', models.IntegerField(blank=True)),
                ('corriente', models.IntegerField(blank=True)),
                ('nivel_sonoro', models.CharField(blank=True, max_length=50)),
                ('dimensiones', models.CharField(blank=True, max_length=50)),
                ('peso', models.IntegerField(blank=True)),
                ('refrigerante', models.CharField(blank=True, max_length=50)),
                ('estado', models.IntegerField(blank=True)),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Bodega')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Bodega')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoFuncionamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRepuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='repuesto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.TipoRepuesto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.TipoFuncionamiento'),
        ),
    ]