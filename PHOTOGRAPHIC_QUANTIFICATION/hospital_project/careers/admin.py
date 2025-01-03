from django.contrib import admin
from .models import positions

class positionfn(admin.ModelAdmin):
    list_display = ("positionname", "baseSalary", "department",)
admin.site.register(positions)

