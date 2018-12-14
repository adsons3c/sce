from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Modelos_PC(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo

status_choices = (
    ('Ativo', 'Ativo'),
    ('Inativo', 'Inativo'),
)
class Computadores(models.Model):

    memoria_choices = (
    ('2GB', '2GB'),
    ('3GB', '3GB'),
    ('4GB', '4GB'),
    ('6GB', '6GB'),
    ('8GB', '8GB'),
    ('16GB', '16GB'),
    ('32GB', '32GB'),
    )
    hd_choices = (
    ('240GB', '240GB'),
    ('250GB', '250GB'),
    ('500GB', '500GB'),
    ('1000GB', '1000GB'),
    ('2000GB', '2000GB'),
    )


    tombamento = models.IntegerField()
    numero_serie = models.CharField(max_length=100)
    sistema_oper = models.CharField(max_length=50)
    licenca_so = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=50)
    processador = models.CharField(max_length=30)
    memoria = models.CharField(max_length=4, choices=memoria_choices, default='4GB')
    hd = models.CharField(max_length=10, choices=hd_choices)
    data_ultima_manutencao = models.DateField(blank=True)
    data_proxima_manutencao = models.DateField(blank=True)
    descricao_manutencao = models.TextField()
    status = models.CharField(max_length=7, choices=status_choices, default='Ativo')
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelos_PC, on_delete=models.CASCADE)


    def __str__(self):
        return self.modelo


class Roteador_Wifi(models.Model):
    modelo = models.CharField(max_length=100)
    tombamento = models.IntegerField()
    numero_serie = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=50)
    senha_admin = models.CharField(max_length=50)
    data_ultima_manutencao = models.DateField()
    data_proxima_manutencao = models.DateField()
    descricao_manutencao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=status_choices, default='Ativo')

    def __str__(self):
        return self.modelo


class Impressora(models.Model):
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    locada = models.BooleanField()
    empresa_locadora = models.CharField(max_length=100)
    data_ultima_manutencao = models.DateField()
    data_proxima_manutencao = models.DateField()
    descricao_manutencao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=status_choices)

    def __str__(self):
        return self.modelo


class Switch(models.Model):
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    senha_admin = models.CharField(max_length=50)
    data_ultima_manutencao = models.DateField()
    data_proxima_manutencao = models.DateField()
    descricao_manutencao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=status_choices)

    def __str__(self):
        return self.modelo
