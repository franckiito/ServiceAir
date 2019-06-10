from django.http import HttpResponse, JsonResponse
from django.http import response
from django.shortcuts import render, redirect
from users.models import Usuario
from users.forms import UsuarioForm, LoginForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q
from producto.models import Bodega, TipoFuncionamiento, Producto, TipoRepuesto, Repuesto
from producto.forms import BodegaForm, TipoFuncionamientoForm, ProductoForm, TipoRepuestoForm, RepuestoForm

# Create your views here.

#region BODEGA OK

#Query que retorna las bodegas
class BodegaQueryset(object):

    def get_bodegas_queryset(self,request):
        bodegas = Bodega.objects.all()
        return bodegas

#vista de bodegas
class ListBodegasView(View):
    def get(self, request):
        bodegas_list = Bodega.objects.all()

        context = {
            "bodegas_list" : bodegas_list
        }
        return render(request,"producto/list_bodegas.html", context)

#Crea una bodega
class CreateBodega(View):

    #@method_decorator(login_required())
    def get(self,request):
        form = BodegaForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'material/add_bodega.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        success_message = ''
        form = BodegaForm(request.POST)

        if form.is_valid():
            
            bodega = Bodega.objects.filter(titulo=form.cleaned_data['nombre'])

            if len(bodega) == 0 : 
                new_bodega = form.save()
                data = { 
                'mensaje': 'La bodega fue registrada correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Bodega' 
                } 
                return JsonResponse(data) 
            else:
                data = { 
                'mensaje': 'La bodega ya existe!', 
                'type' : 'error', 
                'tittle': 'Registro Bodega' 
                } 
                return JsonResponse(data) 
        else:
            data = { 
                'mensaje': 'La bodega no se pudo registrar!', 
                'type' : 'error', 
                'tittle': 'Registro Bodega' 
            } 
            return JsonResponse(data) 

#vista para editar la bodega
class EditBodega(View, BodegaQueryset):
    def get(self,request,pk):
        possible_bodegas = self.get_bodegas_queryset(request).filter(pk=pk)
        bodega = possible_bodegas[0] if len(possible_bodegas) == 1 else None
        if bodega is not None:
            #cargamos el detalle
            context = {
                'form': BodegaForm(instance=bodega),
                'id': bodega.pk,
            }
            return render(request, 'material/edit_bodega.html',context)
        else:
            data = { 
                'mensaje': 'No exite bodega!', 
                'type' : 'error', 
                'tittle': 'Bodega' 
            } 
            return JsonResponse(data) 

    def post(self,request,pk):
        possible_bodegas = self.get_bodegas_queryset(request).filter(pk=pk)
        bodega = possible_bodegas[0] if len(possible_bodegas) == 1 else None
        if bodega is not None:
            form = BodegaForm(request.POST,instance=bodega)
            if form.is_valid():

                bodega = TypeDocument.objects.filter(titulo=form.cleaned_data['nombre'])
                if len(bodega) == 0 : 
                    form.save()
                    data = { 
                    'mensaje': 'La bodega se editó correctamente!.', 
                    'type' : 'success', 
                    'tittle': 'Bodega' 
                    } 
                    return JsonResponse(data) 

                else:
                    data = { 
                    'mensaje': 'La bodega ya existe!.', 
                    'type' : 'error', 
                    'tittle': 'Bodega' 
                    } 
                    return JsonResponse(data)

            else:
                data = { 
                'mensaje': 'No se puedo editar!.', 
                'type' : 'error', 
                'tittle': 'Bodega' 
                } 
                return JsonResponse(data) 

#endregion 

#region TIPO FUNCIONAMIENTO

#Query que retorna los Tipos de Funcionamiento de Repuesto
class TipoFuncionamientoQueryset(object):

    def get_funcionamientos_queryset(self,request):
        funcionamientos = TipoFuncionamiento.objects.all()
        return funcionamientos

#vista de tipos de funcionamientos
class ListTipoFuncionamientosView(View):
    def get(self, request):
        funcionamientos_list = TipoFuncionamiento.objects.all()
        context = {
            "funcionamientos_list" : funcionamientos_list
        }
        return render(request,"producto/list_funcionamientos.html", context)

#endregion

#region PRODUCTO

#Query que retorna los Productos
class ProductoQueryset(object):

    def get_productos_queryset(self,request):
        productos = Producto.objects.all()
        return productos

#vista de los tipos de material
class ListProductosView(View):
    def get(self, request):
        productos_list = Producto.objects.all()

        context = {
            "productos_list" : productos_list
        }
        return render(request,"material/list_productos.html", context)

#endregion

#region TIPO DE REPUESTO

#Query que retorna los Tipos de Repuestos
class TipoRepuestoQueryset(object):

    def get_tipo_repuestos_queryset(self,request):
        tipo_repuestos = TipoRepuesto.objects.all()
        return tipo_repuestos

#vista de los tipos de material
class ListTipoRepuestosView(View):
    def get(self, request):
        tipo_repuestos_list = TipoRepuesto.objects.all()

        context = {
            "tipo_repuestos_list" : tipo_repuestos_list
        }
        return render(request,"material/list_tipo_repuestos.html", context)

#endregion    

#region REPUESTOS

#Query que retorna los Repuestos
class RepuestoQueryset(object):

    def get_repuestos_queryset(self,request):
        repuestos = Repuesto.objects.all()
        return repuestos

#vista de los tipos de material
class ListRepuestosView(View):
    def get(self, request):
        repuestos_list = Repuesto.objects.all()

        context = {
            "repuestos_list" : repuestos_list
        }
        return render(request,"material/list_repuestos.html", context)

#endregion 