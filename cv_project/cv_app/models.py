from django.db import models
from django.urls import reverse

# Create your models here.
# https://docs.djangoproject.com/en/4.1/topics/db/models/

class CV(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length = 20)
    cognome = models.CharField(max_length = 20)
    residenza = models.CharField(max_length = 40)
    skill  = models.CharField(max_length = 30)

    def __str__(self):  #per scegliere cosa visualizzare su admin
        return self.nome + ' ' + self.cognome

    def get_absolute_url(self):
        #slug = models.SlugField(max_length=250, unique_for_date='publish')
        return reverse('home_view',args=[])

class Progetto(models.Model):
    immagine = models.ImageField()
    titolo = models.CharField(max_length = 50)
    descrizione = models.TextField(max_length = 300)

    def __str__(self):  #per scegliere cosa visualizzare su admin
        return self.titolo

    def get_absolute_url(self):
        #slug = models.SlugField(max_length=250, unique_for_date='publish')
        return reverse('home_view',args=[])
