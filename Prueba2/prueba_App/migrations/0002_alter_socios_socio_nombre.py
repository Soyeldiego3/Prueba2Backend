# Generated by Django 4.2.7 on 2023-12-01 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socios',
            name='Socio_Nombre',
            field=models.CharField(max_length=80),
        ),
    ]
