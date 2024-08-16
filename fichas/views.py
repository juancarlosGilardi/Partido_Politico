from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET
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
    dni = request.GET.get('dni', None)
    if dni:
        print(f"Buscando DNI: {dni}")  # Agrega este print para ver si el DNI se está recibiendo correctamente
        try:
            ficha = FichaInscripcion.objects.get(dni=dni)
            data = {
                'nombres': ficha.nombres,
                'apellido_paterno': ficha.apellido_paterno,
                'apellido_materno': ficha.apellido_materno,
                'fecha_nacimiento': ficha.fecha_nacimiento,
                'referido_por': str(ficha.referido_por) if ficha.referido_por else '',
                'lugar_nacimiento': ficha.lugar_nacimiento,
                'telefono_fijo': ficha.telefono_fijo,
                'celular': ficha.celular,
                'email': ficha.email,
                'direccion' : ficha.direccion,
                'distrito': ficha.distrito,
                'provincia': ficha.provincia,
                'departamento' : ficha.departamento,
            }
            return JsonResponse(data)
        except FichaInscripcion.DoesNotExist:
            print("DNI no encontrado.")  # Agrega este print para depurar
            return JsonResponse({'error': 'No se encontró ninguna persona con ese DNI.'}, status=404)
    print("DNI no proporcionado.")  # Agrega este print para depurar
    return JsonResponse({'error': 'DNI no proporcionado.'}, status=400)


def lista_inscritos(request):
    inscritos = FichaInscripcion.objects.all().order_by('-fecha_inscripcion')
    return render(request, 'inv/lista_inscritos.html', {'inscritos': inscritos})

class BaseView(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    
    def handle_no_permission(self):
        messages.error(self.request , "No tienes permiso para acceder a esta página.")
        return redirect('config:home')