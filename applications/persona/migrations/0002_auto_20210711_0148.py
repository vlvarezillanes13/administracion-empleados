# Generated by Django 3.2.5 on 2021-07-11 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_options'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='habilidades')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['-first_name', 'last_name'], 'verbose_name': 'Mi Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AddField(
            model_name='persona',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together={('first_name', 'departamento')},
        ),
    ]
