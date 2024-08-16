from django.urls import path

from .views import get_person_data ,\
    inscripcion , lista_inscritos

app_name = "inv"

urlpatterns = [
    path("inscripcion", inscripcion , name = "inscripcion"),
    path("lista_inscritos", lista_inscritos , name= "lista_inscritos"),
    path('get_person_data/', get_person_data, name='get_person_data'),


]