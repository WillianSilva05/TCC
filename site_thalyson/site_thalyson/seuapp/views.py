import email
from faulthandler import disable
from http.client import HTTPResponse
from operator import truediv

from django.shortcuts import render, redirect
from seuapp.forms import UsersForm, AgendamentoForm, LoginForm
from seuapp.models import Usuario, Agendamento


# Create your views here.
def dologout(request):
	try:
		del request.session['uid']
		return redirect ("logout")
	except KeyError:
		pass
	return render(request, "home.html")
	

def home(request):
	profile = {}
	try:
		profile['uid'] = Usuario.objects.get(id=request.session['uid'])
		profile['custom'] = "Sair"
		print(profile)
	except KeyError:
		profile['custom'] = "Entrar"
	return render(request,'home.html', profile)

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)

def login(request):
	data = {}
	data['login'] = LoginForm()
	return render(request,'login.html',data)


def esqueceuSenha(request):
	data = {}
	data['esqueceuSenha'] = UsersForm()
	return render(request,'esqueceuSenha.html',data)

def novaSenha(request):
	data = {}
	data['novaSenha'] = UsersForm()
	return render(request,'novaSenha.html',data)

def errorLogin(request):
	data = {}
	return render(request,'errorLogin.html',data)

def errorEditar(request):
	data = {}
	return render(request,'errorEditar.html',data)


def logout(request):
	data = {}
	return render(request,'logout.html',data)

def docad(request):
	data = {}
	tabela = Usuario.objects.all()
	form = UsersForm(request.POST or None)
	erro = ''
	for c in tabela:
		if form['usuario'].data == c.usuario :
			return render(request,'userError.html', data)
	for c in tabela:
		if form['email'].data == c.email :
			return render(request,'userError.html', data)
	for c in tabela:
		if form['tel'].data == c.tel:
			return render(request,'userError.html', data)
	if form.is_valid() and erro == '':
		form.save()
	return render(request,'registerSucces.html', data)


def dolog(request):
	if request.method == "POST":
		try:
			u = Usuario.objects.get(usuario=request.POST['usuario'])
		except:
			return redirect("errorLogin")
		print(u.usuario)
		if u.senha == request.POST['senha']:
			request.session['uid'] = u.id
			return redirect('home')
		else:
			return redirect("errorLogin")
	else: 
		return redirect ('login')
	
def profile(request):
	profile = {}
	try:
		profile['perfil'] = UsersForm(instance=Usuario.objects.get(id=request.session['uid']))
		return render(request, 'novaSenha.html', profile)
	except:
		return HTTPResponse("vc não está logado")
	

def doupdate(request):

	form = Usuario.objects.get(id=request.session['uid'])
	if request.POST['confirma_senha'] == form.senha:
		form.senha = request.POST['senha']
		form.usuario = request.POST['usuario']
		form.email = request.POST['email']
	else:
		return redirect('errorEditar')
	form.save()
	return redirect ('home')


def agendamento(request):
	data = {}
	data['agendform'] = AgendamentoForm()
	if request.method == 'POST':
		c = Agendamento(usuario=Usuario.objects.get(id=request.session['uid']), nome = request.POST['nome'], sobrenome = request.POST['sobrenome'], celular = request.POST['celular'], data = request.POST['data'], hora = request.POST['hora'])
		try:
			if request.POST['data'].data == c.data:
				return redirect ("userError")
			else:
				c.save()
		except: 
			pass
		return redirect('agendamento')
	else:
		data['history'] = Agendamento.objects.filter(usuario=request.session['uid'])
		print(data['history'])
		return render(request,'agendamento.html',data)

def edit_coment(request, id):
    c = Agendamento.objects.get(id=id)
    if request.method == 'POST':
        f = AgendamentoForm(request.POST, instance=c)
        f.save()
        return redirect('agendamento')
    else:
        f = AgendamentoForm(instance=c)
        return render(request, 'agendamento.html',{'agendform':f})
	




