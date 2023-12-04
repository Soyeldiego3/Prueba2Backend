from django import forms
from django.core import validators
from .models import Socios
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator

class FormSocios(forms.ModelForm):
    
    Socio_Nombre = forms.CharField(label='Nombre del Socio', widget=forms.TextInput(attrs={'placeholder': 'Nombre del Socio', 'class': 'form-control'}), validators=[validators.MaxLengthValidator(limit_value=80, message='El nombre del socio no puede superar los 80 caracteres!')])
    Socio_Fecha_in = forms.DateField(label='Fecha Inicio', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    ANIO_CHOICES = [(str(anio), str(anio)) for anio in range(1950, 2024)]
    Socio_Anio = forms.ChoiceField(label='Año de Nacimiento', choices=ANIO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    Socio_Telefono = forms.IntegerField(label='Numero Telefonico', widget=forms.TextInput(attrs={'placeholder': '912345678', 'class': 'form-control', 'input_type': 'tel'}), validators=[RegexValidator(regex=r'^\d{1,9}$', message='El número de teléfono no es válido')])
    Socio_Email = forms.EmailField(label='Correo Electronico', widget=forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico', 'class': 'form-control'}), validators=[validate_email])

    SEXO_CHOICES = [ 
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]
    Socio_Sexo = forms.ChoiceField(label='Sexo', widget=forms.Select(attrs={'class': 'form-select'}), choices=SEXO_CHOICES)

    ESTADO_CHOICES = [
        ('Vigente', 'Vigente'),
        ('Suspendido', 'Suspendido'),
        ('Retirado', 'Retirado'),
    ]
    Socio_Estado = forms.ChoiceField(label='Estado', widget=forms.Select(attrs={'class': 'form-select'}), choices=ESTADO_CHOICES)

    Socio_Observacion = forms.CharField(label='Observaciones', required=False, widget=forms.Textarea(attrs={'placeholder': 'Ingrese observaciones', 'class': 'form-control'}))
    
    class Meta:
        model = Socios
        fields = ['Socio_Nombre', 'Socio_Fecha_in', 'Socio_Anio', 'Socio_Telefono', 'Socio_Email', 'Socio_Sexo', 'Socio_Estado', 'Socio_Observacion']


    def clean_Socio_Email(self):
        email = self.cleaned_data.get('Socio_Email')
        dominios = ['gmail.com', 'inacapmail.cl']

        if not any(email.endswith(dominio) for dominio in dominios):
            raise ValidationError("No se permiten correos con este dominio.")


        return email