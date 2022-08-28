from tracemalloc import get_object_traceback
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Recepie

# Create your views here.
def index(request):
    receitas = Recepie.objects.order_by('-publish_datetime').filter(is_published=True)
    
    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita(request, recepie_id):
    receita = get_object_or_404(Recepie, pk=recepie_id)
    dados = {
        'receita': receita
    }
    return render(request, 'receita.html', dados)

def search(request):
    lista_receitas = Recepie.objects.order_by('-publish_datetime').filter(is_published=True)
    if 'search' in request.GET:
        search_name = request.GET['search']
        if search_name:
            lista_receitas = lista_receitas.filter(recepie_name__icontains=search_name)
    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'search.html', dados)
