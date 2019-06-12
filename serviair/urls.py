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

from users.views import Create as CreateUser, ListUsersView, LoginView, LogoutView, UserDetailView, UserEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('principal.urls')),

    #URL's App USERS
    url(r'^adm/new_user$', CreateUser.as_view(), name='create_user'), #url, nuevo user
    url(r'^adm/users$', ListUsersView.as_view(), name='list_users'), #url, lista usuarios
    url(r'^adm/User_Detail(?P<pk>[0-9]+)$', UserDetailView.as_view(), name='user_detail'), #url, Detalle Usuario
    url(r'^adm/user_edit/(?P<pk>[0-9]+)$', UserEditView.as_view(), name='user_edit'), #url, Edita Usuario
    url(r'^login$', LoginView.as_view(), name='users_login'), #url, Login
    url(r'^logout$', LogoutView.as_view(), name='users_logout'), #url, Logout
]
