from django.shortcuts import render

# Create your views here.

def about_view(request):
    return render(request, 'about.html')

def contacto_view(request):
    formulario = contacto_form()
    nombre = "david"
    return render(request, 'contacto.html', {'n':nombre, 'f': formulario} )