from django.db import models
from clientes.models import Cliente

class Aluguel(models.Model):
    ITEM_CHOICES = (
        ('AIR_HOCKEY', 'Air hockey'),
        ('PEBOLIM', 'Pebolim'),
        ('PING_PONG', 'Ping pong'),
        ('CAMA_ELASTICA_2M', 'Cama elástica 2m'),
        ('CAMA_ELASTICA_3M', 'Cama elástica 3m'),
        ('CAMA_ELASTICA_4M', 'Cama elástica 4,5m'),
        ('BASQUETE_ELETRONICO', 'Basquete eletrônico'),
        ('SINUCA', 'Sinuca'),
        ('PISCINA_DE_BOLINHAS', 'Piscina de bolinhas'),
        ('MESAS_E_CADEIRAS', 'Mesas e cadeiras'),
    )

    data_aluguel = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    itens_alugados = models.ManyToManyField('Item', blank=True, related_name='alugueis_relacionados')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'Aluguel {self.pk} de {self.cliente} em {self.data_aluguel}'

    def itens_alugados_str(self):
        return ", ".join([item.nome for item in self.itens_alugados.all()])


class Item(models.Model):
    nome = models.CharField(max_length=50)
    aluguel = models.ManyToManyField(Aluguel, related_name='itens_alugados_relacionados')


    def __str__(self):
        return self.nome
