from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    unidade = models.ForeignKey(Unidade, on_delete=models.DO_NOTHING, default=1)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to='produtos_fotos', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    def get_foto(self):
        if self.foto:
            return self.foto.url
        else:
            return 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fbr%2Fvetores%2Fdesenho-de-um-ovo-de-pascoa-gm165873797-23287855&psig=AOvVaw1Hl9f2X2k0wq9Gj3jXkZ0q&ust=1614786129968000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjHwO6G_-8CFQAAAAAdAAAAABAD'
        
    def get_preco(self):
        return self.preco
    

