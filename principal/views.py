from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView

from servicios.models import TipoServicio
from producto.models import Producto, Repuesto

# Create your views here.

def index(request):
    return render(request,'principal/index.html', {'type_servicios':TipoServicio.objects.all()})

def aires(request):
    return render(request,'producto/products.html', {'productos':Producto.objects.all()})

def repuests(request):
    return render(request,'producto/repuestos.html', {'repuestos':Repuesto.objects.all()})

def admin(request):
    return render(request,'principal/admin.html')

def tec(request):
    return render(request,'principal/tecnico.html')

#Hay que aplicarlo cuando se tenga listo el admin mientras se usara el def admin para 
#desarrollar
""" 
class AdminView(View):
    @method_decorator(login_required())
    def get(self,request):
        return render(request,'admin.html')
"""