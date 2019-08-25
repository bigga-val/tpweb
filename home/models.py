from django.db import models
from django.utils import timezone #for putting the default time of publishing
from datetime import datetime

# Create your models here.
class Sondage(models.Model):
    question = models.CharField(max_length=200)
    date_publication = models.DateTimeField(default= datetime.now)

    def __str__(self):
        return "{0} {1}".format(self.question, self.date_publication)

class Reponse(models.Model):
    sondage = models.ForeignKey(Sondage,  on_delete=models.CASCADE)
    choix = models.CharField(max_length=200)
    nb_votes = models.CharField(max_length=11, null=True)

    def __str__(self):
        return "{0} {1} {2}".format(self.choix, self.nb_votes, self.sondage)

class Candidat(models.Model):
    reponse = models.OneToOneField(Reponse, on_delete=models.SET_NULL, null=True)
    nom =  models.CharField(max_length=50)

    def __str__(self):
        return self.nom