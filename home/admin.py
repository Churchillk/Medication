from django.contrib import admin
from . models import *

class RegMedicine(admin.ModelAdmin):
    list_display = (
        "author", "Disease", "Medication", "Dose", "start", "end", "id"
    )

admin.site.register(Medicine, RegMedicine)