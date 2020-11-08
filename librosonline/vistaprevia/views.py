from django.shortcuts import render

def index(request):
     contenido= { 'nombre_sitio': 'LibrosOnline' }
     return render(request, 'vistaprevia/index.html', contenido)