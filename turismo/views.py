from django.shortcuts import render
from .models import Servicio

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'turismo/servicios.html', {'servicios': servicios})

def login(request):
    return render(request, 'turismo/login.html')
