from django import forms

class CarrosForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    fabricante = forms.CharField(max_length=20)
    modelo = forms.IntegerField()
    color = forms.CharField(max_length=20)

class MotosForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    fabricante = forms.CharField(max_length=20)
    cilindraje = forms.IntegerField()

class CamionesForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    fabricante = forms.CharField(max_length=20)
    carga_maxima = forms.IntegerField()
    numero_ejes = forms.IntegerField()