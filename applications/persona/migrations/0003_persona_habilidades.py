# Generated by Django 3.2.5 on 2021-07-11 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20210711_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
