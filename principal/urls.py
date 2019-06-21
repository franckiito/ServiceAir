from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name = "index"),
    path('adm',views.admin, name = "adm"),
    path('products',views.aires, name = "aires"),
    path('repuests',views.repuests, name = "repuests"),
]