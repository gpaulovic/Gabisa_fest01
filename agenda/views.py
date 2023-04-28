from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Aluguel, Item
from .forms import AluguelForm
from django.db.models import Q

@login_required
def listar_alugueis(request):
    alugueis = Aluguel.objects.all().prefetch_related('itens_alugados')
    return render(request, 'listar_alugueis.html', {'alugueis': alugueis})

@login_required
def novo_aluguel(request):
    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alugueis')
    else:
        form = AluguelForm()
    itens = Item.objects.all() # Obtém todos os itens
    context = {'form': form, 'itens': itens}
    return render(request, 'novo_aluguel.html', context)

@login_required
def detalhes_aluguel(request, pk):
    aluguel = get_object_or_404(Aluguel, pk=pk)
    return render(request, 'detalhes_aluguel.html', {'aluguel': aluguel})


@login_required
def excluir_aluguel(request, pk):
    aluguel = get_object_or_404(Aluguel, pk=pk)
    if request.method == 'POST':
        aluguel.delete()
        return redirect('listar_alugueis')
    return render(request, 'exclusao_aluguel.html', {'aluguel': aluguel})

