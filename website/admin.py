from django.contrib import admin
from .models import Convite, Convidado, Presente, Imagen

# Register your models here.
admin.site.register(Convite)
admin.site.register(Presente)
admin.site.register(Convidado)
admin.site.register(Imagen)