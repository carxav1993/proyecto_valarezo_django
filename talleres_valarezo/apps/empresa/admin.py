from django.contrib import admin
from .models import Empresa, Servicio, Contacto
# Register your models here.
admin.site.register(Empresa)
admin.site.register(Servicio)
admin.site.register(Contacto)