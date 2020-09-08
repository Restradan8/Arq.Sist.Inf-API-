from django.http import HttpResponse
import datetime

def inicio(request):
    mensaje="<html><body><h1>bienvenido a mi sitio web con django <br> <h2>gracias</h2></html></body></h1>"
    return HttpResponse(mensaje)


#pasar parametros atraves de la url 
def parametros(request):
    fecha_actual=datetime.datetime.now()
    mensaje="<html><body><h1>bienvenido a mi sitio web con django <br> <h2>gracias %s</h2></html></body></h1>"%fecha_actual

    return HttpResponse(mensaje)

def calculaEdad(request,a,b):
    suma=a+b

    mensaje="bienvenido   a mi pagina web veos que tienes %s años?</h1>"% suma

    return HttpResponse(mensaje)

