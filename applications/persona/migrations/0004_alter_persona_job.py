# Generated by Django 3.2.5 on 2021-07-11 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_persona_habilidades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='job',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO')], max_length=1, verbose_name='Trabajo'),
        ),
    ]
