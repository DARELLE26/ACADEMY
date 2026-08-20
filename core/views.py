from django.shortcuts import render
#from django .http import HttpResponse

# Create your views here.
def home(request): 
    return HttpResponse('Bienvenue sur ACADEMY')
# def professeurs(request):
   # return HttpResponse('voici nos professeurs')
def professeurs(request):
    professeurs = [
        {
            "nom": "Marie",
            "matiere": "Mathématiques",
            "tarif": 4800
        },
        {
            "nom": "Jean",
            "matiere": "Physique",
            "tarif": 4500
        },
        {
            "nom": "Pierre",
            "matiere": "Chimie",
            "tarif": 4000
        },
        {
            "nom": "Lucie",
            "matiere": "Biologie",
            "tarif": 4200
        },
        {
            "nom": "Sophie",
            "matiere": "Histoire",
            "tarif": 3800
        },
        {
            "nom": "Antoine",
            "matiere": "Géographie",
            "tarif": 3500
        }
    ]
    contexte = {'professeurs': professeurs}
    return render(request, 'Core/professeurs.html', contexte)