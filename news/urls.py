from django.urls import path
from .views import home, articoloDetailView, listaArticoli, index, query_base, giornalistaDetailView

app_name = 'news'

urlpatterns = [
    path('home', home, name="homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path('', index, name="index"),
    path('query_base', query_base, name="query_base"),
     path("giornalista/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    
]