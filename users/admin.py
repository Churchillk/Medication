from django.contrib import admin
from . models import *

class RegProfile(admin.ModelAdmin):
    list_display = (
        "user", "image", "id"
    )
    
admin.site.register(Profile, RegProfile)
