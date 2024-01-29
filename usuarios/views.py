from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants


def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        user = User.objects.filter(username=usuario)
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas não conferem')
            return redirect('cadastro')
        
        if user.exists():
            messages.add_message(request, messages.ERROR, 'Usuário já existe')
            return redirect('cadastro')
        try:
            usuario = User.objects.create_user(usuario, password=senha)
            usuario.save()
            return redirect('cadastro')
        except:
            messages.add_message(request, messages.ERROR, 'Erro ao criar usuário')
            return redirect('cadastro')
    else:
        return render(request, 'cadastro.html')

def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')
        user = auth.authenticate(request, username=usuario, password=senha)
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado com sucesso!')
            return redirect('/produtos/novo_produto')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos!')
            return redirect('cadastro')

    else:
        if request.user.is_authenticated:
            return redirect('novo_produto')
        else:
            return render(request, 'cadastro.html')
        
def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.SUCCESS, 'Deslogado com sucesso!')
    return redirect('/usuarios/logar')
