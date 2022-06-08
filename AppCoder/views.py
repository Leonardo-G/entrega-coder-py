from django.http import HttpResponse
from django.shortcuts import redirect, render
from AppCoder import forms
from AppCoder import models
from .models import Nosotros

def inicio(request):
    
    return render(request, "AppCoder/inicio.html");

def nosotros(request):
    nosotros_list = Nosotros.objects.all()
    return render(request, 'AppCoder/nosotros.html',{'nosotros':nosotros_list})

def busqueda(request):
    if request.GET["model"] == "curso":
        bodyNombre = request.GET["nombre"]
        resultado = models.Curso.objects.filter(nombre__icontains=bodyNombre)
        
        return render(request, "AppCoder/inicio.html", {"resultado": resultado, "bodyNombre": "Curso"})
    
    
    if request.GET["model"] == "profesor":
        bodyNombre = request.GET["nombre"]
        resultado = models.Profesor.objects.filter(nombre__icontains=bodyNombre)
        
        return render(request, "AppCoder/inicio.html", {"resultado": resultado, "bodyNombre": "Profesor"})
    
    if request.GET["model"] == "estudiante":
        bodyNombre = request.GET["nombre"]
        resultado = models.Estudiante.objects.filter(nombre__icontains=bodyNombre)
        
        return render(request, "AppCoder/inicio.html", {"resultado": resultado, "bodyNombre": "Estudiante"})
    
    else: 
        respuesta = "No enviaste datos"
        
    return HttpResponse(respuesta)

def estudiantesForm( request ):
    if( request.method == "POST"):
        formEstudiante = forms.EstudianteForm(request.POST);
        
        if formEstudiante.is_valid():
            informacion = formEstudiante.cleaned_data
 
            estudiante = models.Estudiante(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"])
 
            estudiante.save()
            
            return redirect("estudiantes");  
        
    else:
        formEstudiante = forms.EstudianteForm()
        estudiantes = models.Estudiante.objects.all()
        
        return render(request, "AppCoder/estudiantes.html", {"formEstudiante": formEstudiante, "estudiantes": estudiantes });    

def profesorForm( request ):
    if( request.method == "POST"):
        formProfesor = forms.ProfesorForm(request.POST);
        
        if formProfesor.is_valid():
            informacion = formProfesor.cleaned_data
 
            profesor = models.Profesor(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"], profesion = informacion["profesion"])
 
            profesor.save()
            
            return redirect("profesores");  
        
    else:
        formProfesor = forms.ProfesorForm()
        profesores = models.Profesor.objects.all()
        
        return render(request, "AppCoder/profesores.html", {"formProfesor": formProfesor, "profesores": profesores });    
             
def cursosForm( request ):
    if( request.method == "POST"):
        formCurso = forms.CursoForm(request.POST);
        
        if formCurso.is_valid():
            informacion = formCurso.cleaned_data
 
            curso = models.Curso(nombre = informacion["nombre"], camada = informacion["camada"])
 
            curso.save()
            
            return redirect("cursos");  
        
    else:
        formCurso = forms.CursoForm()
        cursos = models.Curso.objects.all()
        
        return render(request, "AppCoder/cursos.html", {"formCurso": formCurso, "cursos": cursos });    
             