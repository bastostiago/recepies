from tracemalloc import get_object_traceback
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Recepie

# Create your views here.
def index(request):
    receitas = Recepie.objects.all()
    
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
