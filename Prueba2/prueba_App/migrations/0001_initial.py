# Generated by Django 4.2.7 on 2023-12-01 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Socio_Nombre', models.CharField(max_length=50)),
                ('Socio_Fecha_in', models.DateField()),
                ('Socio_Anio', models.IntegerField()),
                ('Socio_Telefono', models.IntegerField()),
                ('Socio_Email', models.EmailField(max_length=254)),
                ('Socio_Sexo', models.CharField(max_length=30)),
                ('Socio_Estado', models.CharField(max_length=30)),
                ('Socio_Observacion', models.CharField(max_length=100)),
            ],
        ),
    ]
