from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Produto, Unidade
from .forms import ProdutoForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants


# Create your views here.
def novo_produto(request):
    if request.user.is_authenticated == False:
        return redirect('/usuarios/cadastro')
        
    if request.method == "GET":
        categoria = Categoria.objects.all()
        unidades = Unidade.objects.all()
        
        return render(request, 'novo_produto.html', {'categorias': categoria, 'unidades': unidades})
        
    else:
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        unidade = request.POST.get('unidade')
        foto = request.FILES.get('foto')
        categoria = Categoria.objects.get(id=categoria)
        unidade = Unidade.objects.get(id=unidade)
        produto = Produto(nome=nome, preco=preco, descricao=descricao, categoria=categoria, foto=foto, unidade=unidade)
        produto.save()
        messages.add_message(request, constants.SUCCESS, 'Produto cadastrado com sucesso!')
        return render(request, 'novo_produto.html')
    
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def editar_produto(request, id):
    
    if request.method == "GET":
        produto = Produto.objects.get(id=id)
        categoria = Categoria.objects.all()
        unidade = Unidade.objects.all()
        return render(request, 'editar_produto.html', {'produto': produto, 'categorias': categoria, 'unidades': unidade})
    else:
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        unidade = request.POST.get('unidade')
        foto = request.FILES.get('foto')
        unidade = Unidade.objects.get(id=unidade)
        categoria = Categoria.objects.get(id=categoria)
        produto = Produto.objects.get(id=id)
        produto.nome = nome
        produto.preco = preco
        produto.descricao = descricao
        produto.categoria = categoria
        produto.unidade = unidade
        if foto:
            produto.foto = foto
        produto.save()
        messages.add_message(request, constants.SUCCESS, 'Produto editado com sucesso!')
        return render(request, 'editar_produto.html', {'produto': produto})
    
