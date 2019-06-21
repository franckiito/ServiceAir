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
        return render(request, 'producto/add_bodega.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        success_message = ''
        form = BodegaForm(request.POST)

        if form.is_valid():
            
            bodega = Bodega.objects.filter(nombre=form.cleaned_data['nombre'])

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
            return render(request, 'producto/edit_bodega.html',context)
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

                bodega = Bodega.objects.filter(nombre=form.cleaned_data['nombre'].lower())
                if len(bodega) <= 1 : 
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

#region TIPO FUNCIONAMIENTO OK

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

#Crea una Tipo de Funcionamiento
class CreateTipoFuncionamiento(View):

    #@method_decorator(login_required())
    def get(self,request):
        form = TipoFuncionamientoForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'producto/add_funcionamiento.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        success_message = ''
        form = TipoFuncionamientoForm(request.POST)

        if form.is_valid():
            
            func = TipoFuncionamiento.objects.filter(nombre=form.cleaned_data['nombre'])

            if len(func) == 0 : 
                new_func = form.save()
                data = { 
                'mensaje': 'El funcionamiento fue registrado correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Tipo Funcionamiento' 
                } 
                return JsonResponse(data) 
            else:
                data = { 
                'mensaje': 'El funcionamiento ya existe!', 
                'type' : 'error', 
                'tittle': 'Registro Tipo Funcionamiento' 
                } 
                return JsonResponse(data) 
        else:
            data = { 
                'mensaje': 'La bodega no se pudo registrar!', 
                'type' : 'error', 
                'tittle': 'Registro Tipo Funcionamiento' 
            } 
            return JsonResponse(data) 

#vista para editar el tipo de funcionamiento
class EditTipoFuncionamiento(View, TipoFuncionamientoQueryset):
    def get(self,request,pk):
        possible_funcionamientos = self.get_funcionamientos_queryset(request).filter(pk=pk)
        func = possible_funcionamientos[0] if len(possible_funcionamientos) == 1 else None
        if func is not None:
            #cargamos el detalle
            context = {
                'form': TipoFuncionamientoForm(instance=func),
                'id': func.pk,
            }
            return render(request, 'producto/edit_funcionamiento.html',context)
        else:
            data = { 
                'mensaje': 'No exite Funcionamiento!', 
                'type' : 'error', 
                'tittle': 'Tipo de Funcionamiento' 
            } 
            return JsonResponse(data) 

    def post(self,request,pk):
        possible_funcionamientos = self.get_funcionamientos_queryset(request).filter(pk=pk)
        func = possible_funcionamientos[0] if len(possible_funcionamientos) == 1 else None
        if func is not None:
            form = TipoFuncionamientoForm(request.POST,instance=func)
            if form.is_valid():

                func = TipoFuncionamiento.objects.filter(nombre=form.cleaned_data['nombre'])
                if len(func) == 0 : 
                    form.save()
                    data = { 
                    'mensaje': 'El funcionamiento se editó correctamente!.', 
                    'type' : 'success', 
                    'tittle': 'Tipo de Funcionamiento' 
                    } 
                    return JsonResponse(data) 

                else:
                    data = { 
                    'mensaje': 'El funcionamiento ya existe!.', 
                    'type' : 'error', 
                    'tittle': 'Tipo de Funcionamiento' 
                    } 
                    return JsonResponse(data)

            else:
                data = { 
                'mensaje': 'No se puedo editar!.', 
                'type' : 'error', 
                'tittle': 'Tipo de Funcionamiento' 
                } 
                return JsonResponse(data) 

#endregion

#region PRODUCTO OK

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
        return render(request,"producto/list_productos.html", context)

#Crea un Producto
class CreateProducto(View):

    #@method_decorator(login_required())
    def get(self,request):
        form = ProductoForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'producto/add_producto.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        form = ProductoForm(request.POST, request.FILES)
        msg = []
        if form.is_valid():
            
            form.save()
            msg.append("Doc creado correctamente")

        else:
            msg.append("DocForm no valido")

        context = { 'form': form,
            'msg': msg, 
        }
        return HttpResponse(request,'producto/add_producto.html',context)
            
"""
    data = { 
    'mensaje': 'El Producto fue registrado correctamente.', 
    'type' : 'success', 
    'tittle': 'Registro Producto' 
    } 
    return JsonResponse(data)
else:
    data = { 
        'mensaje': 'El Producto no se pudo registrar!', 
        'type' : 'error', 
        'tittle': 'Registro Producto' 
    } 
    return JsonResponse(data)
"""

#vista para editar el producto
class EditProducto(View, ProductoQueryset):
    def get(self,request,pk):
        possible_productos = self.get_productos_queryset(request).filter(pk=pk)
        prod = possible_productos[0] if len(possible_productos) == 1 else None
        if prod is not None:
            #cargamos el detalle
            context = {
                'form': ProductoForm(instance=prod),
                'id': prod.pk,
            }
            return render(request, 'producto/edit_producto.html',context)
        else:
            data = { 
                'mensaje': 'No exite el Producto!', 
                'type' : 'error', 
                'tittle': 'Producto' 
            } 
            return JsonResponse(data) 

    def post(self,request,pk):
        possible_productos = self.get_productos_queryset(request).filter(pk=pk)
        prod = possible_productos[0] if len(possible_productos) == 1 else None
        msg = []
        if prod is not None:
            form = ProductoForm(request.POST,request.FILES,instance=prod)
            if form.is_valid():

                form.save()
                msg.append("El producto fue editado correctamente")

            else:
                msg.append("No se pudo editar el producto")
        else:
            msg.append("El producto no existe")
        
        context = { 'form': form,
            'msg': msg, 
        }
        return render(request, 'producto/edit_producto.html',context)
"""
    data = { 
    'mensaje': 'El Producto se editó correctamente!.', 
    'type' : 'success', 
    'tittle': 'Producto' 
    } 
    return JsonResponse(data)

else:
    data = { 
    'mensaje': 'No se puedo editar!.', 
    'type' : 'error', 
    'tittle': 'Producto' 
    } 
    return JsonResponse(data) 
"""

#endregion

#region TIPO DE REPUESTO OK

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
            "type_repuestos_list" : tipo_repuestos_list
        }
        return render(request,"producto/list_type_repuestos.html", context)

#Crea un Tipo de Repuesto
class CreateTipoRepuesto(View):

    #@method_decorator(login_required())
    def get(self,request):
        form = TipoRepuestoForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'producto/add_type_repuesto.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        success_message = ''
        form = TipoRepuestoForm(request.POST)

        if form.is_valid():
            
            tyr = TipoRepuesto.objects.filter(nombre=form.cleaned_data['nombre'])

            if len(tyr) == 0 : 
                new_tyr = form.save()
                data = { 
                'mensaje': 'El Tipo de Repuesto fue registrado correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Tipo de Repuesto' 
                } 
                return JsonResponse(data) 
            else:
                data = { 
                'mensaje': 'El Tipo de Repuesto ya existe!', 
                'type' : 'error', 
                'tittle': 'Registro Tipo de Repuesto' 
                } 
                return JsonResponse(data) 
        else:
            data = { 
                'mensaje': 'El Tipo de Repuesto no se pudo registrar!', 
                'type' : 'error', 
                'tittle': 'Registro Tipo de Repuesto' 
            } 
            return JsonResponse(data)

#vista para editar el Tipo de Respuesto
class EditTipoRepuesto(View, TipoRepuestoQueryset):
    def get(self,request,pk):
        possible_tipo_repuestos = self.get_tipo_repuestos_queryset(request).filter(pk=pk)
        tyr = possible_tipo_repuestos[0] if len(possible_tipo_repuestos) == 1 else None
        if tyr is not None:
            #cargamos el detalle
            context = {
                'form': TipoRepuestoForm(instance=tyr),
                'id': tyr.pk,
            }
            return render(request, 'producto/edit_tipo_repuesto.html',context)
        else:
            data = { 
                'mensaje': 'No exite el Tipo de Repuesto!', 
                'type' : 'error', 
                'tittle': 'Tipo de Repuesto' 
            } 
            return JsonResponse(data) 

    def post(self,request,pk):
        possible_tipo_repuestos = self.get_tipo_repuestos_queryset(request).filter(pk=pk)
        tyr = possible_tipo_repuestos[0] if len(possible_tipo_repuestos) == 1 else None
        if tyr is not None:
            form = TipoRepuestoForm(request.POST,instance=tyr)
            if form.is_valid():

                form.save()
                data = { 
                'mensaje': 'El Tipo de Repuesto se editó correctamente!.', 
                'type' : 'success', 
                'tittle': 'Tipo de Repuesto' 
                } 
                return JsonResponse(data) 

            else:
                data = { 
                'mensaje': 'No se puedo editar!.', 
                'type' : 'error', 
                'tittle': 'Tipo de Repuesto' 
                } 
                return JsonResponse(data) 


#endregion    

#region REPUESTOS OK

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
        return render(request,"producto/list_repuestos.html", context)

#Crea un Repuesto
class CreateRepuesto(View):

    #@method_decorator(login_required())
    def get(self,request):
        form = RepuestoForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'producto/add_repuesto.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        success_message = ''
        form = RepuestoForm(request.POST,request.FILES)
        msg = []
        if form.is_valid():
            repuesto = Repuesto.objects.filter(nombre=form.cleaned_data['nombre'])
            if len(repuesto) == 0 :
                form.save()
                msg.append("Repuesto fue creado correctamente")
            else:
                msg.append("El repuesto ya exite!")
        else:
            msg.append("DocForm no valido")
        context = { 'form': form,
            'msg': msg, 
        }
        return render(request,'producto/add_repuesto.html',context)

"""
if form.is_valid():
    
    repuesto = Repuesto.objects.filter(nombre=form.cleaned_data['nombre'])

    if len(repuesto) == 0 : 
        new_repuesto = form.save()
        data = { 
        'mensaje': 'El Repuesto fue registrado correctamente.', 
        'type' : 'success', 
        'tittle': 'Registro Repuesto' 
        } 
        return JsonResponse(data) 
    else:
        data = { 
        'mensaje': 'El Repuesto ya existe!', 
        'type' : 'error', 
        'tittle': 'Registro Repuesto' 
        } 
        return JsonResponse(data) 
else:
    data = { 
        'mensaje': 'El Repuesto no se pudo registrar!', 
        'type' : 'error', 
        'tittle': 'Registro Repuesto' 
    } 
    return JsonResponse(data)
"""

#vista para editar el tipo de funcionamiento
class EditRepuesto(View, RepuestoQueryset):
    def get(self,request,pk):
        possible_repuestos = self.get_repuestos_queryset(request).filter(pk=pk)
        repuesto = possible_repuestos[0] if len(possible_repuestos) == 1 else None
        if repuesto is not None:
            #cargamos el detalle
            context = {
                'form': RepuestoForm(instance=repuesto),
                'id': repuesto.pk,
            }
            return render(request, 'producto/edit_repuesto.html',context)
        else:
            data = { 
                'mensaje': 'No exite Repuesto!', 
                'type' : 'error', 
                'tittle': 'Repuesto' 
            } 
            return JsonResponse(data) 

    def post(self,request,pk):
        possible_repuestos = self.get_repuestos_queryset(request).filter(pk=pk)
        repuesto = possible_repuestos[0] if len(possible_repuestos) == 1 else None
        msg = []
        if repuesto is not None:
            form = RepuestoForm(request.POST,request.FILES,instance=repuesto)
            if form.is_valid():
                form.save()
                msg.append("El repuesto fue editado correctamente")
            else:
                msg.append("El formulario no es valido")    
        else:
            msg.append("El repuesto no existe")
        context = { 'form': form,
            'msg': msg, 
        }
        return render(request,'producto/edit_repuesto.html',context)

"""
if repuesto is not None:
    form = RepuestoForm(request.POST,instance=repuesto)
    if form.is_valid():

        repuesto = Repuesto.objects.filter(nombre=form.cleaned_data['nombre'])
        if len(repuesto) == 0 : 
            form.save()
            data = { 
            'mensaje': 'El Repuesto se editó correctamente!.', 
            'type' : 'success', 
            'tittle': 'Repuesto' 
            } 
            return JsonResponse(data) 

        else:
            data = { 
            'mensaje': 'El Repuesto ya existe!.', 
            'type' : 'error', 
            'tittle': 'Repuesto' 
            } 
            return JsonResponse(data)

    else:
        data = { 
        'mensaje': 'No se puedo editar!.', 
        'type' : 'error', 
        'tittle': 'Repuesto' 
        } 
        return JsonResponse(data) 
"""
#endregion 
