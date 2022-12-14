from distutils.command.upload import upload
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Relogio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, max_length=150)

    def __str__(self):
        return self.nome