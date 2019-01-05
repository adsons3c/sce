from django.db import models

'''Modelo de Setor'''
class Setor(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    sigla = models.CharField(max_length=30, unique=True)

    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        self.sigla = self.sigla.upper()
        super(Setor, self).save(force_insert, force_update)

    def __str__(self):
        return self.nome

'''Modelo de PC'''
class Modelos_PC(models.Model):
    marca = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100, unique=True)

    def save(self, force_insert=False, force_update=False):
        self.modelo = self.modelo.upper()
        self.marca = self.marca.upper()
        super(Modelos_PC, self).save(force_insert, force_update)

    def __str__(self):
        return self.modelo

status_choices = (
    ('Ativo', 'Ativo'),
    ('Inativo', 'Inativo'),
    ('Manutenção', 'Manutenção')
)

'''Modelo de Computadores'''
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


    tombamento = models.IntegerField(unique=True)
    numero_serie = models.CharField(max_length=100, unique=True)
    sistema_oper = models.CharField(max_length=50)
    licenca_so = models.CharField(max_length=100, unique=True)
    ip = models.GenericIPAddressField(unique=True)
    mac = models.CharField(max_length=50, unique=True)
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

'''Modelo do Roteador Wifi'''
class Roteador_Wifi(models.Model):
    modelo = models.CharField(max_length=100)
    tombamento = models.IntegerField(unique=True)
    numero_serie = models.CharField(max_length=100, unique=True)
    ip = models.GenericIPAddressField(unique=True)
    mac = models.CharField(max_length=50, unique=True)
    senha_admin = models.CharField(max_length=50)
    data_ultima_manutencao = models.DateField()
    data_proxima_manutencao = models.DateField()
    descricao_manutencao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=status_choices, default='Ativo')

    def __str__(self):
        return self.modelo

'''Modelo de Impressora'''
class Impressora(models.Model):
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    ip = models.GenericIPAddressField(unique=True)
    locada = models.BooleanField()
    empresa_locadora = models.CharField(max_length=100)
    data_ultima_manutencao = models.DateField()
    data_proxima_manutencao = models.DateField()
    descricao_manutencao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=status_choices, default='Ativo')

    def __str__(self):
        return self.modelo

'''Modelo do Switch'''
class Switch(models.Model):
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    ip = models.GenericIPAddressField(unique=True)
    senha_admin = models.CharField(max_length=50)
    data_ultima_manutencao = models.DateField()
    data_proxima_manutencao = models.DateField()
    descricao_manutencao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=status_choices, default='Ativo')

    def __str__(self):
        return self.modelo
