from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) #crea l'istanza conj l'input dell'utente
        
        if form.is_valid(): #effettua la validazione
            user = form.save()
            login(request, user)
            return redirect('/')    #eventumente da personalizzare
    
    else:   #richiesta di tipo get mostro il form vuoto
        form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'form': form})
