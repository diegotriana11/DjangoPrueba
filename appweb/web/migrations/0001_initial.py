# Generated by Django 2.2.1 on 2019-08-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoMunicipio', models.PositiveSmallIntegerField()),
                ('NombreMunicipio', models.CharField(max_length=35)),
                ('EstadoMunicipio', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoRegion', models.PositiveSmallIntegerField()),
                ('NombreRegion', models.CharField(max_length=35)),
                ('EstadoRegion', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('Municipio', models.ManyToManyField(blank=True, to='web.Municipio')),
            ],
        ),
    ]
