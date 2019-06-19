# Generated by Django 2.1.4 on 2019-05-26 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BITACORA_GANADO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('lugar', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CONTROL_GANADO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arete', models.CharField(max_length=10)),
                ('motivo', models.CharField(choices=[('Pesaje', 'Pesaje'), ('Servicio', 'Servicio'), ('Destete', 'Destete')], max_length=15)),
                ('descripcion', models.TextField()),
                ('lugar', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CULTIVO_ALMACEN_BAJA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(default='0', max_length=30)),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EN_BODEGA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EN_PROCESO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hectareas', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('pe', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='GANADO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('arete', models.CharField(max_length=10)),
                ('siniga', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=10)),
                ('propietario', models.CharField(max_length=20)),
                ('ganadera', models.CharField(max_length=20)),
                ('no_padre', models.IntegerField(blank=True, null=True)),
                ('no_madre', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.CharField(max_length=15)),
                ('tipo_nacimiento', models.CharField(choices=[('Uníparo', 'Uníparo'), ('Gemelar MH', 'Gemelar MH'), ('Gemelar HH', 'Gemelar HH'), ('Gemelar MM', 'Gemelar MM'), ('Múltiple', 'Múltiple')], max_length=15)),
                ('tipo_parto', models.CharField(choices=[('Normal', 'Normal'), ('Distónico', 'Distónico'), ('Difícil', 'Difícil'), ('Cesárea', 'Cesárea')], max_length=15)),
                ('localizacion_fierro', models.CharField(max_length=10)),
                ('estado', models.CharField(choices=[('Vendida', 'Vendida'), ('Viva', 'Viva'), ('Muerta', 'Muerta')], max_length=10)),
                ('peso', models.FloatField()),
                ('galeria_venta', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='Ganado', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='GANADO_BITACORA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=15, null=True)),
                ('arete', models.CharField(blank=True, max_length=10, null=True)),
                ('siniga', models.CharField(blank=True, max_length=10, null=True)),
                ('sexo', models.CharField(blank=True, max_length=10, null=True)),
                ('propietario', models.CharField(blank=True, max_length=20, null=True)),
                ('ganadera', models.CharField(blank=True, max_length=20, null=True)),
                ('no_padre', models.IntegerField(blank=True, null=True)),
                ('no_madre', models.IntegerField(blank=True, null=True)),
                ('tipo_nacimiento', models.CharField(blank=True, max_length=15, null=True)),
                ('tipo_parto', models.CharField(blank=True, max_length=15, null=True)),
                ('localizacion_fierro', models.CharField(blank=True, max_length=10, null=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='Ganado', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HISTORIAL_VENTAS_BOVINO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_bovino', models.CharField(default='0000', max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('total', models.FloatField()),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HISTORIAL_VENTAS_CERDOS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('total', models.FloatField()),
                ('fecha', models.DateField()),
                ('estado', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HISTORIAL_VENTAS_CULTIVO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(default='0', max_length=30)),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField()),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HISTORIAL_VENTAS_LECHE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('total', models.FloatField()),
                ('fecha', models.DateField()),
                ('estado', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='REGISTRO_AGRICOLA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='en_proceso',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.REGISTRO_AGRICOLA'),
        ),
        migrations.AddField(
            model_name='bitacora_ganado',
            name='bovino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.GANADO'),
        ),
    ]