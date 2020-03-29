from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return f'{self.marca}/{self.modelo} - {self.placa}'


class Parametro(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros Gerais'
