from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario')
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=25)
    

    def __str__(self):
        return self.nome


class Sala(models.Model):
    numero = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    # Outros campos para informações da sala

    def __str__(self):
        return (self.numero + ' - '+ self.descricao)
    
class Chave(models.Model):
    disponivel = models.BooleanField(default=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='chaves')
    

    def __str__(self):
        return (self.sala.numero + ' - '+ self.sala.descricao)


class AluguelChave(models.Model):
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE , related_name='alugueis')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_aluguel = models.DateTimeField(auto_now=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.chave.sala.numero + ' - ' + self.chave.sala.descricao 
