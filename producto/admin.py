from django.contrib import admin

# Register your models here.

from producto.models import Bodega, Producto,  Repuesto


class BodegaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'direccion',)
    list_filter = ('nombre', 'descripcion', 'direccion',)
    search_fields = ('nombre', 'descripcion', 'direccion',)
    ordering = ('nombre',)

    add_fieldsets = (
        (None, {
            'classes':('wide',),

        })
    )


class RepuestoAdmin(admin.ModelAdmin):
    list_display = ('bodega', 'tipo', 'producto', 'nombre', 'descripcion', 'stock', 'imagen',)
    list_filter = ('bodega', 'tipo', 'producto', 'nombre', 'descripcion', 'stock', 'imagen',)
    search_fields = ('bodega', 'tipo', 'producto', 'nombre', 'descripcion', 'stock', 'imagen',)
    ordering = ('bodega',)

    add_fieldsets = (
        (None, {
            'classes':('wide',),

        })
    )

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('bodega', 'tipo', 'sku', 'nombre', 'descripcion', 'modelo', 'precio', 'stock', 'estado', 'imagen',)
    list_filter = ('bodega', 'tipo', 'sku', 'nombre', 'descripcion', 'modelo', 'precio', 'stock', 'estado', 'imagen',)
    search_fields = ('bodega', 'tipo', 'sku', 'nombre', 'descripcion', 'modelo', 'precio', 'stock', 'estado', 'imagen',)
    ordering = ('precio',)

    add_fieldsets = (
        (None, {
            'classes':('wide',),

        })
    )

admin.site.register(Bodega,BodegaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Repuesto,RepuestoAdmin)