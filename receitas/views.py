from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Receita
# Create your views here.
def index(request):

    '''receitas = {
        1:'Lasanha',
        2:'Sopa De Legumes',
        3:'Sorvete De Prestigio',
        4:'Danone',
        5:'Filé Mignon',
        6:'Batatas Fritas',
        7:'Frango Assado'
    }

    dados ={
        'nome_das_receitas': receitas
    }'''
    #receitas = Receita.objects.all()
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    dados = {
        'receitas': receitas
    }
    #return HttpResponse("<h1>Receitas</h1><h2>Seja bem - vindo Thiago Carrenho Ferreira!!!</h2>")
    #return render(request, "index.html", {'nome_receita': 'Sorvete De Prestigio'})
    return render(request, "index.html", dados)
    

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    receita_a_exibir = {
        'receita' : receita
        }

    return render(request, "receita.html", receita_a_exibir)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    if 'pesquisa' in request.GET:
        nome_a_buscar = request.GET['pesquisa']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'buscar.html', dados)