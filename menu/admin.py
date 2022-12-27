from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Menu, MainMenu

admin.site.register(MainMenu)
admin.site.register(Menu, MPTTModelAdmin)
