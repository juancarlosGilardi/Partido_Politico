from django.db import models
from django.utils import timezone
from urllib.parse import quote
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django_userforeignkey.models.fields import UserForeignKey


from .managers import UsuarioManager

class Usuario(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('direccion email'), max_length=254, unique=True)
    first_name = models.CharField(_('nombres'), max_length=30, blank=True)
    last_name = models.CharField(_('apellidos'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('es staff'), default=False,
        help_text=_('Indica si el usuario puede iniciar sesión en admin '))
    is_active = models.BooleanField(_('activo'), default=True,
        help_text=_('Designa si este usuario debe ser tratado como activo'
                    'Deseleccione esto en lugar de eliminar cuentas.'))
    date_joined = models.DateTimeField(_('fecha registro'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_absolute_url(self):
        return "/users/%s" % quote(self.email)
    
    def get_full_name(self):
        full_name = "%s %s" % (self.first_name,self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
    
    
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    #uc = models.ForeignKey(UsuarioManager, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True,null=True)

    class Meta:
        abstract=True


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = UserForeignKey(auto_user_add=True,related_name='+')
    um = UserForeignKey(auto_user=True,related_name='+')

    class Meta:
        abstract=True



class Idioma(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Idiomas"

    def __str__(self):
        return self.nombre


class Frase(models.Model):
    idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE)
    autor = models.CharField(max_length=50,default="Anónimo")
    frase = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Frases"

    def __str__(self):
        return "{} - {}".format(self.autor,self.idioma)