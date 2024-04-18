from django.shortcuts import render
from .models import Flan

# Create your views here.
def indice(request):

    # Obtiene flanes públicos
    postres_publicos = Flan.objects.filter(is_private = False)

    return render(request, "index.html", {
        'postres_publicos': postres_publicos
    })

def bienvenido(request):

    # Obtiene flanes privados
    postres_privados = Flan.objects.filter(is_private = True)

    return render(request, "welcome.html", {
        'postres_privados': postres_privados
    })

def acerca(request):
    return render(request, "about.html", {})
