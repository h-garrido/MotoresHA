# Generated by Django 4.1.2 on 2023-07-11 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motores_ha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_reserva', models.IntegerField()),
                ('estado', models.CharField(default='Pendiente', max_length=20)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motores_ha.vehiculo')),
            ],
        ),
    ]
