from django.contrib import admin
from .models import Doador
from .models import Medico

admin.site.register(Doador)
admin.site.register(Medico)