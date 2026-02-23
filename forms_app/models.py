from django.db import models

class Contatto(models.Model):
    nome = models.CharField(max_length=100, default=None)
    cognome = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=200, default=None)
    contenuto = models.TextField(default=None)
