# Generated by Django 2.1.4 on 2018-12-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actives_IT', '0009_auto_20181214_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadores',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], default='Ativo', max_length=7),
        ),
        migrations.AlterField(
            model_name='impressora',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], max_length=7),
        ),
        migrations.AlterField(
            model_name='roteador_wifi',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], default='Ativo', max_length=7),
        ),
        migrations.AlterField(
            model_name='switch',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], max_length=7),
        ),
    ]