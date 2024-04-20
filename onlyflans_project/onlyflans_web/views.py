from django.shortcuts import render
from django.http import HttpResponseRedirect

#from .forms import ContactFormForm # Importacion del formulario del modelo

from .forms import ContactFormModelForm  # Importa el nuevo formulario
from .models import ContactForm, Flan

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

def contacto(request):

    # Verifica si la solicitud correpsonde a POST
    if request.method == 'POST':

        # Imprime en la terminal la información del formulario (como parte del desarrollo)
        print(request.POST)

        # form = ContactFormForm(request.POST) # Crea instancia del formulario con los datos ingresados

        form = ContactFormModelForm(request.POST)

        # Si es válido el formulario, redirige a página de inicio
        if form.is_valid():            

            # contact_form = ContactForm.objects.create(**form.cleaned_data)

            form.save()    

            return HttpResponseRedirect('/exito')
        
        else:
            # Mensaje de error para la terminal
            print('El formato no es válido')
    
    # De lo contrario crea instancia vacía para que se muestre en la página
    else:
        # form = ContactFormForm()

        form = ContactFormModelForm()

    return render(request, "contact.html", {'form': form})

def exito(request):
    return render(request, "success.html", {})
