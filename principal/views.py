from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView

# Create your views here.

def index(request):
    return render(request,'principal/index.html')

def admin(request):
    return render(request,'principal/admin.html')

#Hay que aplicarlo cuando se tenga listo el admin mientras se usara el def admin para 
#desarrollar
""" 
class AdminView(View):
    @method_decorator(login_required())
    def get(self,request):
        return render(request,'admin.html')
"""