# Generated by Django 3.1.3 on 2020-11-30 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0004_cotizacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='Fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
