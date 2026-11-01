from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):

    #nombre="Claudio"
    #apellido="Serrano"

    p1=Persona("Claudios","Serrano R.")
    ahora=datetime.datetime.now()
    #temasDelCurso=["Plantillas","Modelos","Formularios","Vistas"]

    temasDelCurso=["Plantillas","Modelos","Formularios","Vistas"]

    #doc_externo=open("C:/Python/Proyectos/django/Django01/Django01/plantillas/primeraplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    ##doc_externo=loader.get_template('primeraplantilla.html')
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasDelCurso})

    #documento=plt.render(ctx)
    ##documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasDelCurso})

    return render(request,"primeraplantilla.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasDelCurso})

def despedida(request):
    return HttpResponse("Adios desde Django")

def cursoC(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "cursoC.html",{"dameFecha":fecha_actual})

def cursoCss(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "cursoCss.html",{"dameFecha":fecha_actual})

def damefecha(request):
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actual: %s
    <h1>
    <body>
    <html>""" % fecha_actual

    return HttpResponse(documento)

def calculaedad(request,edad,agno):
    #edad_actual=56
    periodo=agno-2026
    edad_futura=edad+periodo
    
    documento="""<html>
    <body>
    <h2>
    En el año: %s
    tendrás: %s años
    <h2>
    <body>
    <html>""" % (agno,edad_futura)

    return HttpResponse(documento)


