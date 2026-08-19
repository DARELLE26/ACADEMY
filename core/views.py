from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.
def home(request): 
    return HttpResponse('Bienvenue sur ACADEMY')
def professeurs(request):
    return HttpResponse('voici nos professeurs')
def contact(request):
    return HttpResponse('Contacter ACADEMY')
