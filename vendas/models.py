from django.db import models
from produtos.models import Produto
# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
    
class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        valor = self.produto.preco * self.quantidade
        return valor
    
    def __str__(self):
        return self.produto.nome
    
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    itens_venda = models.ManyToManyField(ItemVenda)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Venda {self.pk} - {self.comprador.nome}"

    def save(self, *args, **kwargs):
        valor_total = 0
        for item in self.itens_venda.all():
            valor_total += item.valor
        self.valor_total = valor_total
        super().save(*args, **kwargs)

    