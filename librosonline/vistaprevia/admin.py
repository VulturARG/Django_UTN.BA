from django.contrib import admin
from vistaprevia.models import Producto

class ProductoAdmin(admin.ModelAdmin):

    fields = ['fecha_publicacion','producto', 'ruta_imagen']
    list_display = ['producto', 'fecha_publicacion', 'ruta_imagen']
    ordering = ['-fecha_publicacion']
    list_filter = ('producto', 'fecha_publicacion')

admin.site.register(Producto,ProductoAdmin)
