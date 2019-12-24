from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Inicio')

def contact(request):
    return HttpResponse('Contacto')