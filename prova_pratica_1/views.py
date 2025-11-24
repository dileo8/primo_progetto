from django.shortcuts import render

def index(request):
    return render(request, "prova_pratica_1/index.html")

def differenza(request):
    return render(request, "prova_pratica_1/differenza.html")

def pari_dispari(request):
    return render(request, "prova_pratica_1/pari_dispari.html")