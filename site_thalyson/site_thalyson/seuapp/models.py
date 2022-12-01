from django.db import models

# Create your models here.
class Usuario(models.Model):
    cpf = models.CharField(max_length=14)
    usuario = models.CharField(max_length=16)
    email = models.CharField(max_length=256)
    nascimento = models.DateField()
    tel = models.CharField(max_length=15)
    senha = models.CharField(max_length=16)

class Agendamento(models.Model):
    FuncionariosChoices = [
    ("BlackJack", "Junin Black"),
    ("Pedro", "Pedro lucas")]

    TIME_CHOICES = [
    ("08:00 às 09:00", "08:00 às 09:00"),
    ("09:00 às 10:00", "09:00 às 10:00"),
    ("10:00 às 11:00", "10:00 às 11:00"),
    ("11:00 às 12:00", "11:00 às 12:00"),
    ("13:00 às 14:00", "13:00 às 14:00"),
    ("14:00 às 15:00", "14:00 às 15:00"),
    ("15:00 às 16:00", "15:00 às 16:00"),
    ("16:00 às 17:00", "16:00 às 17:00"),
    ("17:00 às 18:00", "17:00 às 18:00"),
    ("18:00 às 19:00", "18:00 às 19:00"),
]
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 16)
    sobrenome = models.CharField(max_length = 30)
    tel = models.CharField(max_length = 15)
    funcionarios = models.CharField(max_length=100, choices=FuncionariosChoices, blank=True, null=True)
    data = models.DateField()
    hora = models.CharField(max_length=100, choices = TIME_CHOICES)

class Servicos(models.Model):
    servico = models.CharField(max_length=120) 
    valor = models.IntegerField()
    preenchido = models.ManyToManyField(Agendamento, through='Servicos_preenchido')

class Servicos_preenchido(models.Model):
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)