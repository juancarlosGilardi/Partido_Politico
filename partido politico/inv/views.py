from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import FichaInscripcionForm
from .apis_net_pe import ApisNetPe
from .models import FichaInscripcion

def inscripcion(request):
    if request.method == 'POST':
        form = FichaInscripcionForm(request.POST)
        if form.is_valid():
            ficha = form.save()
            messages.success(request, f'Inscripción exitosa para {ficha.nombres} {ficha.apellido_paterno}')
            return redirect('inv:lista_inscritos')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = FichaInscripcionForm()
    return render(request, 'inv/inscripcion.html', {'form': form})

def get_person_data(request):
    if request.method == 'GET':
        dni = request.GET.get('dni', '')
        api_client = ApisNetPe()
        result = api_client.get_person(dni)
        if result:
            return JsonResponse({
                'nombres': result.get('nombres', ''),
                'apellido_paterno': result.get('apellidoPaterno', ''),
                'apellido_materno': result.get('apellidoMaterno', ''),
                'fecha_nacimiento': result.get('fechaNacimiento', ''),
            })
        else:
            return JsonResponse({'error': 'No se encontraron datos para el DNI proporcionado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# def inscripcion_exitosa(request):
#     return render(request, 'inv/inscripcion_exitosa.html')

def lista_inscritos(request):
    inscritos = FichaInscripcion.objects.all().order_by('-fecha_inscripcion')
    return render(request, 'inv/lista_inscritos.html', {'inscritos': inscritos})

class BaseView(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    
    def handle_no_permission(self):
        messages.error(self.request , "No tienes permiso para acceder a esta página.")
        return redirect('config:home')

