from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

# Lista de produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'product/lista_produtos.html', {'produtos': produtos})

# Detalhes de um produto
def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'product/detalhe_produto.html', {'produto': produto})

# Criar produto
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'product/criar_produto.html', {'form': form})

# Editar produto
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'product/editar_produto.html', {'form': form})

# Deletar produto
def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'product/deletar_produto.html', {'produto': produto})
