from django.http import HttpResponse, JsonResponse
from django.http import response
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q

from users.models import Usuario
from users.forms import UsuarioForm, LoginForm

from servicios.forms import TipoServicioForm, SolicitudForm, AgendamientoForm
from servicios.models import TipoServicio, Solicitud, Agendamiento

# Create your views here.

#region TipoServicio OK

#Query que retorna los TipoServicio
class TipoServiciosQueryset(object):

    def get_types_queryset(self,request):
        types = TipoServicio.objects.all()
        return types

#vista para listar los TipoServicio
class ListTipoServiciosView(View):
    def get(self, request):
        types_list = TipoServicio.objects.all()
        context = {
            "types_list" : types_list
        }
        return render(request,"servicios/list_type_servicio.html", context)

#Crear TipoServicio
class CreateTipoServicio(View):

    #@method_decorator(login_required())
    def get(self,request):
        """
        esto cmuestra un formulario para crear un TipoServicio
        :param request:
        :return:
        """
        form = TipoServicioForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'servicios/add_type_servicio.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        """
        esto cmuestra un formulario para crear un TipoServicio
        :param request:
        :return:
        """
        success_message = ''

        form = TipoServicioForm(request.POST)
        if form.is_valid():

            form.save()
            data = { 
                'mensaje': 'El Tipo de servicio fue registrado correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Tipo de servicio' 
            } 
            return JsonResponse(data)
        else:
            data = { 
                'mensaje': 'Formulario invalido!', 
                'type' : 'error', 
                'tittle': 'Registro Tipo de servicio' 
            } 
            return JsonResponse(data)

#editar de un TipoServicio
class EditTipoServicioView(View, TipoServiciosQueryset):
    def get(self,request,pk):
        """
        Carga la página de detalle de una tipo
        :param request:
        :param pk:
        :return: HttpResponse
        """
        possible_types = self.get_types_queryset(request).filter(pk=pk)
        tipo = possible_types[0] if len(possible_types) == 1 else None
        if tipo is not None:
            #cargamos el detalle
            context = {
                'form': TipoServicioForm(instance=tipo),
                'id': tipo.pk,
            }
            return render(request, 'servicios/edit_type_servicio.html',context)
        else:
            return response.HttpResponseNotFound('No existe el Tipo de servicio')#error 404

    def post(self,request,pk):
        """
        esto cmuestra un formulario para crear una foto y la crea
        :param request:
        :return:
        """

        possible_types = self.get_types_queryset(request).filter(pk=pk)
        tipo = possible_types[0] if len(possible_types) == 1 else None
        if tipo is not None:
            form = TipoServicioForm(request.POST,instance=tipo)
            if form.is_valid():
                form.save()
                data = { 
                    'mensaje': 'El Tipo de servicio fue editado correctamente.', 
                    'type' : 'success', 
                    'tittle': 'Registro Tipo de servicio' 
                } 
                return JsonResponse(data)
            else:
                data = { 
                    'mensaje': 'Error al editar.', 
                    'type' : 'error', 
                    'tittle': 'Registro Tipo de servicio' 
                } 
                return JsonResponse(data)





#endregion 

#region Solicitud OK

#Query que retorna los Solicitudes
class SolicitudesQueryset(object):

    def get_servicios_queryset(self,request):
        solicitudes = Solicitud.objects.all()
        return solicitudes

#vista para listar los Solicitudes
class ListSolicitudesView(View):
    def get(self, request):
        solicitudes_list = Solicitud.objects.all()
        context = {
            "solicitudes_list" : solicitudes_list
        }
        return render(request,"servicios/list_solicitudes.html", context)

#Crear Solicitud
class CreateSolicitudView(View, TipoServiciosQueryset):

    #@method_decorator(login_required())
    def get(self,request,pk):
        """
        esto cmuestra un formulario para crear un Solicitud
        :param request:
        :return:
        """
        possible_types = TipoServicio.objects.filter(pk=pk)
        tipo = possible_types[0] if len(possible_types) == 1 else None
        if tipo is not None:
            soli = Solicitud()
            soli.tipo = tipo
            form = SolicitudForm(instance=soli)

            context = {
                'form': form,
                'success_message': ''
            }
            return render(request, 'servicios/add_solicitud.html', context)
        else:
            return response.HttpResponseNotFound('No existe la Solicitud')#error 404

    #@method_decorator(login_required())
    def post(self,request,pk):
        """
        esto cmuestra un formulario para crear un Solicitud
        :param request:
        :return:
        """
        possible_types = self.get_types_queryset(request).filter(pk=pk)
        tipo = possible_types[0] if len(possible_types) == 1 else None
        if tipo is not None:
            soli_clie = Solicitud()
            soli_clie.cliente = request.user #Asigna propietario
            soli_clie.tipo = tipo
            form = SolicitudForm(request.POST, instance=soli_clie)
            
            if form.is_valid():
                new_solic = form.save()
                data = { 
                    'mensaje': 'La Solicitud fue registrada correctamente.', 
                    'type' : 'success', 
                    'tittle': 'Registro Solicitud' 
                } 
                return JsonResponse(data)
                
            else:
                data = { 
                    'mensaje': 'Error al registrar!', 
                    'type' : 'error', 
                    'tittle': 'Registro Solicitud' 
                } 
                return JsonResponse(data)   
        else:
            data = { 
                'mensaje': 'No existe el Tipo de servicio !', 
                'type' : 'error', 
                'tittle': 'Tipo Servicio' 
            } 
            return JsonResponse(data)

#editar de un TipoServicio
class EditSolicitudView(View, TipoServiciosQueryset):
    def get(self,request,pk):
        """
        Carga la página de detalle de una Solicitud
        :param request:
        :param pk:
        :return: HttpResponse
        """
        possible_solicitudes = self.get_servicios_queryset(request).filter(pk=pk)
        soli = possible_solicitudes[0] if len(possible_solicitudes) == 1 else None
        if soli is not None:
            #cargamos el detalle
            context = {
                'form': SolicitudForm(instance=soli),
                'id': soli.pk,
            }
            return render(request, 'servicios/edit_solicitud.html',context)
        else:
            return response.HttpResponseNotFound('No existe la Solicitud')#error 404

    def post(self,request,pk):
        """
        esto cmuestra un formulario para editar una Solicitud
        :param request:
        :return:
        """

        possible_solicitudes = self.get_servicios_queryset(request).filter(pk=pk)
        soli = possible_solicitudes[0] if len(possible_solicitudes) == 1 else None
        if soli is not None:
            form = SolicitudForm(request.POST,instance=soli)
            if form.is_valid():
                form.save()
                data = { 
                    'mensaje': 'La Solicitud fue editado correctamente.', 
                    'type' : 'success', 
                    'tittle': 'Edición Solicitud' 
                } 
                return JsonResponse(data)
            else:
                data = { 
                    'mensaje': 'Error al editar.', 
                    'type' : 'error', 
                    'tittle': 'Edición Solicitud' 
                } 
                return JsonResponse(data)


#endregion

#region Agendamiento OK

#Query que retorna los Agendamiento
class AgendamientosQueryset(object):
    def get_agendamientos_queryset(self,request):
        agendamientos = Agendamiento.objects.all()
        return agendamientos

#vista para listar los Agendamiento
class ListAgendamientosView(View):
    def get(self, request):
        agendamientos_list = Agendamiento.objects.all()
        context = {
            "agendamientos_list" : agendamientos_list
        }
        return render(request,"servicios/list_agendamientos.html", context)

#Crear Agendamiento
class CreateAgendamientoView(View):

    #@method_decorator(login_required())
    def get(self,request):
        """
        esto cmuestra un formulario para crear un Agendamiento
        :param request:
        :return:
        """
        form = AgendamientoForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'servicios/add_agendamiento.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        """
        esto cmuestra un formulario para crear un Agendamiento
        :param request:
        :return:
        """

        form = AgendamientoForm(request.POST)
        if form.is_valid():
            new = form.save()
            data = { 
                'mensaje': 'El Agendamiento fue registrado correctamente.', 
                'type' : 'success', 
                'tittle': 'Registro Agendamiento' 
            } 
            return JsonResponse(data)
            
        else:
            data = { 
                'mensaje': 'Error al registrar!', 
                'type' : 'error', 
                'tittle': 'Registro Agendamiento' 
            } 
            return JsonResponse(data)

#editar de un TipoServicio
class EditAgendamientoView(View, AgendamientosQueryset):
    def get(self,request,pk):
        """
        Carga la página de detalle de una Agendamiento
        :param request:
        :param pk:
        :return: HttpResponse
        """
        possible_agendamientos = self.get_agendamientos_queryset(request).filter(pk=pk)
        agen = possible_agendamientos[0] if len(possible_agendamientos) == 1 else None
        if agen is not None:
            #cargamos el detalle
            context = {
                'form': AgendamientoForm(instance=agen),
                'id': agen.pk,
            }
            return render(request, 'servicios/edit_agendamiento.html',context)
        else:
            return response.HttpResponseNotFound('No existe el Agendamiento')#error 404

    def post(self,request,pk):
        """
        esto cmuestra un formulario para editar una Solicitud
        :param request:
        :return:
        """

        possible_agendamientos = self.get_agendamientos_queryset(request).filter(pk=pk)
        agen = possible_agendamientos[0] if len(possible_agendamientos) == 1 else None
        if agen is not None:
            form = AgendamientoForm(request.POST,instance=agen)
            if form.is_valid():
                form.save()
                data = { 
                    'mensaje': 'El Agendamiento fue editado correctamente.', 
                    'type' : 'success', 
                    'tittle': 'Edición Agendamiento' 
                } 
                return JsonResponse(data)
            else:
                data = { 
                    'mensaje': 'Error al editar.', 
                    'type' : 'error', 
                    'tittle': 'Edición Agendamiento' 
                } 
                return JsonResponse(data)


#endregion
