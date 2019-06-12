from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView

# Create your views here.

def index(request):
    return render(request,'principal/index.html')