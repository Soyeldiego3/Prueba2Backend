from django.shortcuts import redirect, render
from prueba_App.models import Socios
from .forms import FormSocios


# Create your views here.

def RenderIndex(request):
    return render(request, 'Index.html')

def ListarSocios(request):
    Socio = Socios.objects.all().order_by('-Socio_Fecha_in')[:15]

    data = {'Socio': Socio}
    return render(request, 'Socios.html', data)

def AgregarSocio(request):
    if (request.method == "POST" ):
        form = FormSocios(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/socios')
    else:
        form = FormSocios()
  
    data = {'form' :form }
    return render(request, 'Agregar.html', data)

def EditarSocio(request , id):

    Soc = Socios.objects.get(id = id)
    form = FormSocios(instance = Soc)

    if (request.method == "POST" ):
        form = FormSocios(request.POST, instance = Soc)
        if(form.is_valid()):
            form.save()
            return redirect('/socios')
  
    data = {'form' :form }
    return render(request, 'Agregar.html', data)

def EliminarSocio(request, id):
    Soc = Socios.objects.get(id = id)
    Soc.delete()
    return redirect('/socios')