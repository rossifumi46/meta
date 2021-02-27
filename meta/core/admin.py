from django.contrib import admin

from .models import Psychoterapist, Method, Data

admin.site.register(Psychoterapist)
admin.site.register(Method)
admin.site.register(Data)