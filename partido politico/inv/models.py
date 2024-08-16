from django.db import models
from bases.models import ClaseModelo

class FichaInscripcion(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    ESTADO_CIVIL_CHOICES = [
        ('S', 'Soltero/a'),
        ('C', 'Casado/a'),
        ('V', 'Viudo/a'),
        ('D', 'Divorciado/a'),
        ('O', 'Otro'),
    ]
    GRADO_INSTRUCCION_CHOICES = [
        ('P', 'Primaria'),
        ('S', 'Secundaria'),
        ('T', 'Técnico'),
        ('U', 'Universitario'),
    ]

    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    referido_por = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='referidos')
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    telefono_fijo = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20)
    email = models.EmailField()
    dni = models.CharField(max_length=8, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)
    grado_instruccion = models.CharField(max_length=1, choices=GRADO_INSTRUCCION_CHOICES)
    profesion = models.CharField(max_length=100, blank=True, null=True)  
    direccion = models.CharField(max_length=200)
    distrito = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    centro_laboral = models.CharField(max_length=200, blank=True, null=True)
    cargo_laboral = models.CharField(max_length=100, blank=True, null=True)
    direccion_laboral = models.CharField(max_length=200)
    distrito_laboral = models.CharField(max_length=100)
    provincia_laboral = models.CharField(max_length=100)
    departamento_laboral = models.CharField(max_length=100)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dni} - {self.nombres} {self.apellido_paterno} {self.apellido_materno}"
