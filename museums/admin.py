# museums/admin.py

from django.contrib import admin
from museums.models import Museum

class MuseumAdmin(admin.ModelAdmin):
    pass

admin.site.register(Museum, MuseumAdmin)
