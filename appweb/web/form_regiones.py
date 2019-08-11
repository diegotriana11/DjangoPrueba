from django import forms
from appweb.web.models import Region

class RegionForm(forms.ModelForm):

	class Meta:
		model  = Region
		fields = [
			'CodigoRegion',
			'NombreRegion',
			'EstadoRegion',
			'Municipio'
		]
		labels = {
			'CodigoRegion':'Codigo',
			'NombreRegion':'Nombre',
			'EstadoRegion':'Estado',
			'Municipio':'Municipio'
		}
		widgets = {
			'CodigoRegion':forms.TextInput(attrs={'class':'form-control'}),
			'NombreRegion':forms.TextInput(attrs={'class':'form-control'}),
			'EstadoRegion':forms.Select(attrs={'class':'form-control'}),
			'Municipio':forms.CheckboxSelectMultiple(),
		}