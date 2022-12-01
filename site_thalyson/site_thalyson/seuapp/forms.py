from cgitb import text
from faulthandler import disable
from multiprocessing.resource_sharer import stop
from django.forms import DateInput, ModelForm, TimeInput
from django import forms
from tkinter import Widget
from seuapp.models import Usuario, Agendamento, Servicos

# Create the form class.


CORTE_UM = [
    ("Navalhado", "navalhado"),
]

CORTE_DOIS = [
    ("Tesoura", "tesoura"),
]

CORTE_TRES = [
    ("Maquina", "maquina"),
]

CORTE_QUATRO = [
    ("Tesoura/maquina", "tesoura/maquina"),
]
CORTE_CINCO = [
    ("Degrade", "degrade"),
]

CORTE_BARBA = [
    ("Barba", "barba"),
]

CORTE_SOBRANCELHA = [
    ("Sobrancelha", "sobrancelha"),
]



class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirma_senha = forms.CharField(widget=forms.PasswordInput)
    confirma_nova_senha = forms.CharField(widget=forms.PasswordInput)
    nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu número de telefone', 'onkeypress': 'formatNumber(event)', 'maxlength': '15', 'required' : 'True'}))
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'email', 'senha', 'confirma_senha','confirma_nova_senha','tel', 'nascimento']

class LoginForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']


class AgendamentoForm(ModelForm):
    FuncionariosChoice = [
    ("BlackJack", "Junin Black"),
    ("Pedro", "Pedro lucas"),]

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
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.ChoiceField(choices = TIME_CHOICES,)
    funcionarios = forms.ChoiceField(choices = FuncionariosChoice)
    class Meta:
        model = Agendamento
        fields = ['nome', 'sobrenome', 'tel', 'data', 'hora', 'funcionarios']    

class ServicosForm(ModelForm):
    servico = forms.CharField() 
    valor = forms.IntegerField()
    class Meta:
        model = Servicos
        fields = ['servico', 'valor']   








