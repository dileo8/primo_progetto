from django.shortcuts import render

voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

def index(request):
    return render(request, "voti/index.html")

def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    
    context = {
        "materie":materie
    }
    return render(request, "voti/view_a.html", context)

def view_b(request):    
    context = {
        "voti":voti
    }
    return render(request, "voti/view_b.html", context)

def view_c(request):
    medie = {}
    
    for studente, dati in voti.items():
        somma = 0
        i = 0
        for materia, voto, assenza in dati:
            somma+=voto
            i+=1
        media = somma/i
        medie[studente] = media
        
    context = {
        "medie":medie
    }
    
    return render(request, "voti/view_c.html", context)

def view_d(request):
    max = 0
    min = 11
    votiMax =[]
    votiMin = []
    
    for studente, dati in voti.items():
        for materia, voto, assenza in dati:
            if voto > max:
                max = voto
            elif voto < min:
                min = voto
                
    for studente, dati in voti.items():
        for materia, voto, assenza in dati:
            if voto == max:
                votiMax.append((materia, studente))
            elif voto == min:
                votiMin.append((materia, studente))
    context = {"max": max,
               "min": min,
               "votiMax": votiMax,
               "votiMin": votiMax,
               }
    return render(request, "voti/view_d.html", context)