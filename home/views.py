from django.shortcuts import render_to_response, render
from . import models


# Create your views here.
def homepage(request):
    sondage = models.Sondage.objects.all()

    return render_to_response('index.html', {'sondage': sondage, 'titre': 'on voit la liste de sondage'})
