from django import forms   # importo  formulario de django
from .models import Persona # importo mi modelo

class Personaform(forms.ModelForm):# es tipo modelform porq es un formulario
	class Meta: # indica a ue model le va hacer referencia en este caso a persona
		model = Persona
		fields = '__all__' # si deseo especificar todos los campos de mi modelo
		# fields = ('nombre','apellidos',) # si deseo especificar todos los campos de mi modelo
