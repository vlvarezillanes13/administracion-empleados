# Generated by Django 3.2.5 on 2021-07-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_empleado_hoja_vida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='hoja_vida',
        ),
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre Completo'),
        ),
    ]
