from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Computadores(models.Model):
    modelo = models.CharField(max_length=100)
    tombamento = models.IntegerField()
    numero_serie = models.CharField(max_length=100)
    sistema_oper = models.CharField(max_length=50)
    licenca_so = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=50)
    data_ultima_manutencao = models.DateField(blank=True)
    data_proxima_manutencao = models.DateField(blank=True)
    descricao_manutencao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)


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

    def __str__(self):
        return self.modelo
