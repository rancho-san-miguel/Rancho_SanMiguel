# Generated by Django 2.1.4 on 2019-04-01 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('no_padre', models.IntegerField()),
                ('no_madre', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('tipo_nacimiento', models.CharField(choices=[('Uníparo', 'Uníparo'), ('Gemelar MH', 'Gemelar MH'), ('Gemelar HH', 'Gemelar HH'), ('Gemelar MM', 'Gemelar MM'), ('Multiple', 'Multiple')], max_length=15)),
                ('tipo_parto', models.CharField(choices=[('Normal', 'Normal'), ('Distónico', 'Distónico'), ('Difícil', 'Difícil'), ('Cesárea', 'Cesárea')], max_length=15)),
                ('localizacion_fierro', models.CharField(max_length=10)),
                ('estado', models.CharField(choices=[('Vendida', 'Vendida'), ('Viva', 'Viva'), ('Muerta', 'Muerta')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
