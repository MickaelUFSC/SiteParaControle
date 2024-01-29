from django.shortcuts import render, redirect, get_object_or_404
from .models import Venda, Cliente
from produtos.models import Produto
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

# Create your views here.
def nova_venda(request):
    if request.user.is_authenticated == False:
        return redirect('/usuarios/cadastro')
        
    if request.method == "GET":
        clientes = Cliente.objects.all()
        produtos = Produto.objects.all()
        return render(request, 'nova_venda.html', {'clientes': clientes, 'produtos': produtos})
        
    else:
        cliente = request.POST.get('cliente')
        cliente = Cliente.objects.get(id=cliente)
        venda = Venda(cliente=cliente)
        venda.save()
        messages.add_message(request, constants.SUCCESS, 'Venda cadastrada com sucesso!')
        return render(request, 'nova_venda.html')