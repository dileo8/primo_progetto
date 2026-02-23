from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormContatto

def contatti(request):
    #se la richiesta è di tipo POST, possiamo processare i dati
    if request.method == "POST":
        #creiamo l'istanza del form e la popoliamo con i dati della POST request
        form = FormContatto(request.POST)
        #is_valid() controlla se il form inserito è valido
        if form.is_valid():
            #possiamo utilizzare i dati validi
            #tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validi e convertirli in tipi standard di Python
            print("Il form è valido!")
            print("NOME: ",form.cleaned_data["nome"])
            print("COGNOME: ",form.cleaned_data["cognome"])
            print("EMAIL: ",form.cleaned_data["email"])
            print("CONTENUTO: ",form.cleaned_data["contenuto"])
            
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)
            
            #ringrazio l'utente per averci contattato - volendo possiamo effettuare un redirect a una pagina specifica
            return HttpResponse("<h1>grazie per averci contattato!</h1>")
        
        #se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form = FormContatto()
    
    #arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta (con metodo GET), o se il form non è valido e ha errori
    context = {"form": form}
    return render(request, "contatto.html", context)

from django.shortcuts import render
from .models import Contatto

def lista_contatti(request):
    contatti = Contatto.objects.all()
    return render(request, "lista_contatti.html", {"contatti": contatti})
        

