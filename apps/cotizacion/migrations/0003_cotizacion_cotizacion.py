# Generated by Django 3.1.3 on 2020-11-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0002_auto_20201129_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='Cotizacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=22),
            preserve_default=False,
        ),
    ]
