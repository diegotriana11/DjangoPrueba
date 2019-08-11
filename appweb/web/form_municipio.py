from django import forms
from appweb.web.models import Municipio
class MunicipioForm(forms.ModelForm):

	class Meta:
		model  = Municipio
		fields = [
			'CodigoMunicipio',
			'NombreMunicipio',
			'EstadoMunicipio'
		]
		labels = {
			'CodigoMunicipio':'Codigo',
			'NombreMunicipio':'Nombre',
			'EstadoMunicipio':'Estado'
		}
		widgets = {
			'CodigoMunicipio': forms.TextInput(attrs={'class':'form-control'}),
			'NombreMunicipio': forms.TextInput(attrs={'class':'form-control'}),
			'EstadoMunicipio': forms.Select(attrs={'class':'form-control'}),
		}