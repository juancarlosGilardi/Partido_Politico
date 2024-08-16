from fichas import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('inscripcion/', views.inscripcion, name='inscripcion'),
    path('get_person_data/', views.get_person_data, name='get_person_data'),
    path('',include(('bases.urls','bases'), namespace='bases')),
    path('fichas/',include(('fichas.urls','fichas'), namespace='fichas')),
    path('select2/', include('django_select2.urls')),
    path('admin/', admin.site.urls),
]
