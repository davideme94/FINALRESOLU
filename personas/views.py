from django.shortcuts import render
from .models import Persona

def index(request):
    dni = request.GET.get('dni')
    persona = Persona.objects.filter(dni=dni).first() if dni else None
    documentos = persona.documentos.all() if persona else []

    return render(request, 'index.html', {
        'persona': persona,
        'documentos': documentos,
        'dni': dni,
    })
