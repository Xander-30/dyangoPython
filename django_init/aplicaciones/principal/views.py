from django.shortcuts import render,redirect

# Create your views here.
from .models import Persona
from.forms import Personaform

def inicio(request):
	personas = Persona.objects.all()
	contexto = {
            'personas':personas
	}
	return render(request,'index.html',contexto)

#template formulario
def crearPersona(request):
    if request.method == 'GET':
        form = Personaform()
        contexto = {
             'form':form
        }

    else:
        form = Personaform(request.POST)
        contexto = {
             'form':form
        }
        if form.is_valid():#validacion del formulario si es valida
           form.save() #guardame el formulario
           return redirect('index')#redireccionalo a la ruta del archivo index
    return render(request,'crear_persona.html',contexto)
	
def editarPersona(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
	    form = Personaform(instance = persona)
	    contexto = {
             'form':form
       } 
    else:
         form= Personaform(request.POST,instance = persona)
         contexto = {
              'form':form
         }
         if form.is_valid():
         	form.save()
         	return redirect('index')
    return render(request,'crear_persona.html',contexto)


def eliminarpersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')










