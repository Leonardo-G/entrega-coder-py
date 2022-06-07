from django.urls  import path
from AppCoder import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("estudiantes/", views.estudiantesForm, name="estudiantes"),
    path("profesores/", views.profesorForm, name="profesores"),
    path("cursos/", views.cursosForm, name="cursos"),
    path("buscar/", views.busqueda, name="buscar")
]