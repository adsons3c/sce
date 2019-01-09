# Generated by Django 2.1.5 on 2019-01-09 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tombamento', models.IntegerField(unique=True)),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('sistema_oper', models.CharField(max_length=50)),
                ('licenca_so', models.CharField(max_length=100, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('mac', models.CharField(max_length=50, unique=True)),
                ('processador', models.CharField(max_length=30)),
                ('memoria', models.CharField(choices=[('2GB', '2GB'), ('3GB', '3GB'), ('4GB', '4GB'), ('6GB', '6GB'), ('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB')], default='4GB', max_length=4)),
                ('hd', models.CharField(choices=[('240GB', '240GB'), ('250GB', '250GB'), ('500GB', '500GB'), ('1000GB', '1000GB'), ('2000GB', '2000GB')], max_length=10)),
                ('data_ultima_manutencao', models.DateField(blank=True, null=True)),
                ('data_proxima_manutencao', models.DateField(blank=True, null=True)),
                ('descricao_manutencao', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], default='Ativo', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Impressora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('locada', models.BooleanField()),
                ('empresa_locadora', models.CharField(max_length=100)),
                ('data_ultima_manutencao', models.DateField(blank=True, null=True)),
                ('data_proxima_manutencao', models.DateField(blank=True, null=True)),
                ('descricao_manutencao', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], default='Ativo', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Modelos_PC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=10, unique=True)),
                ('modelo', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roteador_Wifi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('tombamento', models.IntegerField(unique=True)),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('mac', models.CharField(max_length=50, unique=True)),
                ('senha_admin', models.CharField(max_length=50)),
                ('data_ultima_manutencao', models.DateField(blank=True, null=True)),
                ('data_proxima_manutencao', models.DateField(blank=True, null=True)),
                ('descricao_manutencao', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], default='Ativo', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True)),
                ('sigla', models.CharField(max_length=30, unique=True)),
                ('range_inicial', models.GenericIPAddressField(unique=True)),
                ('range_final', models.GenericIPAddressField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('senha_admin', models.CharField(max_length=50)),
                ('data_ultima_manutencao', models.DateField(blank=True, null=True)),
                ('data_proxima_manutencao', models.DateField(blank=True, null=True)),
                ('descricao_manutencao', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Manutenção', 'Manutenção')], default='Ativo', max_length=7)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actives_IT.Setor')),
            ],
        ),
        migrations.AddField(
            model_name='roteador_wifi',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actives_IT.Setor'),
        ),
        migrations.AddField(
            model_name='impressora',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actives_IT.Setor'),
        ),
        migrations.AddField(
            model_name='computadores',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actives_IT.Modelos_PC'),
        ),
        migrations.AddField(
            model_name='computadores',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actives_IT.Setor'),
        ),
    ]
