from django import forms
from django_select2.forms import ModelSelect2Widget
from .models import FichaInscripcion

class FichaInscripcionForm(forms.ModelForm):
    referido_por = forms.ModelChoiceField(
    queryset=FichaInscripcion.objects.all(),
    required=False,
    widget=forms.Select(attrs={'class': 'form-control'})
)

    class Meta:
        model = FichaInscripcion
        fields = [
            'dni', 'nombres', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'referido_por',
            'lugar_nacimiento', 'telefono_fijo', 'celular', 'email', 'sexo', 'estado_civil',
            'grado_instruccion', 'profesion', 'direccion', 'distrito', 'provincia', 
            'departamento', 'centro_laboral', 'cargo_laboral', 'direccion_laboral',
            'distrito_laboral', 'provincia_laboral', 'departamento_laboral',
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'dni': forms.TextInput(attrs={'id': 'dni', 'maxlength': '8'}),
            'sexo': forms.RadioSelect(),
            'estado_civil': forms.Select(),
            'grado_instruccion': forms.Select(),
            'email': forms.EmailInput(attrs={'type': 'email'}),
            'celular': forms.TextInput(attrs={'type': 'tel'}),
            'telefono_fijo': forms.TextInput(attrs={'type': 'tel'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not isinstance(self.fields[field].widget, (forms.RadioSelect, forms.CheckboxSelectMultiple)):
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if not dni.isdigit() or len(dni) != 8:
            raise forms.ValidationError("El DNI debe ser un número de 8 dígitos.")
        return dni

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if FichaInscripcion.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email

    def clean_celular(self):
        celular = self.cleaned_data.get('celular')
        if not celular.isdigit() or len(celular) != 9:
            raise forms.ValidationError("El número de celular debe tener 9 dígitos.")
        return celular
