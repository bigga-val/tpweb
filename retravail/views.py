from django.shortcuts import render

def index(requete):
    return render(request = requete, template_name="index.html")


