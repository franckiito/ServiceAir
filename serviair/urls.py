"""serviair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from users.views import Create as CreateUser, ListUsersView, LoginView, LogoutView, UserDetailView, UserEditView, ListTiposView, CreateTipoUsuario, EditTipoView, RegUserView
from producto.views import *
from servicios.views import *


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('principal.urls')),

    #URL's App USERS
    url(r'^user/new_user$', CreateUser.as_view(), name='create_user'), #url, nuevo user
    url(r'^users$', ListUsersView.as_view(), name='list_users'), #url, lista usuarios
    url(r'^user/User_Detail(?P<pk>[0-9]+)$', UserDetailView.as_view(), name='user_detail'), #url, Detalle Usuario
    url(r'^user/edit/(?P<pk>[0-9]+)$', UserEditView.as_view(), name='user_edit'), #url, Edita Usuario
    url(r'^login$', LoginView.as_view(), name='users_login'), #url, Login
    url(r'^logout$', LogoutView.as_view(), name='users_logout'), #url, Logout
    url(r'^registrar$', RegUserView.as_view(), name='registrar'), #url del registro de clientes

    url(r'^type_user/add$', CreateTipoUsuario.as_view(), name='create_type_user'), #url, nuevo tipo user
    url(r'^type_user$', ListTiposView.as_view(), name='list_type_user'), #url, lista tipo user
    url(r'^type_user/edit/(?P<pk>[0-9]+)$', EditTipoView.as_view(), name='edit_type_user'), #url, Edita Usuario

    #URL's App PRODUCTO
    url(r'^bodegas$', ListBodegasView.as_view(), name='list_bodegas'), #url, lista bodegas
    url(r'^bodega/add$', CreateBodega.as_view(), name='add_bodega'), #url, nueva bodega
    url(r'^bodega/edit/(?P<pk>[0-9]+)$', EditBodega.as_view(), name='edit_bodega'), #url, Edita bodega
    url(r'^funcionamientos$', ListTipoFuncionamientosView.as_view(), name='list_funcionamientos'), #url, lista tipo funcionamientos
    url(r'^funcionamiento/add$', CreateTipoFuncionamiento.as_view(), name='add_funcionamiento'), #url, nuevo tipo funcionamiento
    url(r'^funcionamiento/edit/(?P<pk>[0-9]+)$', EditTipoFuncionamiento.as_view(), name='edit_funcionamiento'), #url, Edita funcionamiento
    
    url(r'^productos$', ListProductosView.as_view(), name='list_productos'), #url, lista productos
    url(r'^producto/add$', CreateProducto.as_view(), name='add_producto'), #url, nuevo producto
    url(r'^producto/edit/(?P<pk>[0-9]+)$', EditProducto.as_view(), name='edit_producto'), #url, Edita producto
    url(r'^repuestos$', ListRepuestosView.as_view(), name='list_repuestos'), #url, lista repuestos
    url(r'^repuesto/add$', CreateRepuesto.as_view(), name='add_repuesto'), #url, nuevo repuesto
    url(r'^repuesto/edit/(?P<pk>[0-9]+)$', EditRepuesto.as_view(), name='edit_repuesto'), #url, Edita repuesto
    url(r'^type_repuestos$', ListTipoRepuestosView.as_view(), name='list_type_repuestos'), #url, lista tipo repuestos
    url(r'^type_repuesto/add$', CreateTipoRepuesto.as_view(), name='add_type_repuesto'), #url, nuevo tipo repuesto
    url(r'^type_repuesto/edit/(?P<pk>[0-9]+)$', EditTipoRepuesto.as_view(), name='edit_type_repuesto'), #url, Edita type repuesto

    #URL's App SERVICIOS
    url(r'^servicios$', ListTipoServiciosView.as_view(), name='list_type_servicios'), #url, lista servicios
    url(r'^servicio/add$', CreateTipoServicio.as_view(), name='add_type_servicio'), #url, nuevo servicio
    url(r'^servicio/edit/(?P<pk>[0-9]+)$', EditTipoServicioView.as_view(), name='edit_type_servicio'), #url, Edita servicio
    url(r'^solicitudes$', ListSolicitudesView.as_view(), name='list_solicitudes'), #url, lista solicitudes
    url(r'^solicitud/add$', CreateSolicitudView.as_view(), name='add_solicitud'), #url, nueva solicitud
    url(r'^solicitud/edit/(?P<pk>[0-9]+)$', EditSolicitudView.as_view(), name='edit_solicitud'), #url, Edita solicitud
    url(r'^agendas$', ListAgendamientosView.as_view(), name='list_agendas'), #url, lista agendas
    url(r'^agenda/add$', CreateAgendamientoView.as_view(), name='add_agenda'), #url, nueva agenda
    url(r'^agenda/edit/(?P<pk>[0-9]+)$', EditAgendamientoView.as_view(), name='edit_agenda'), #url, Edita agenda
] 

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
