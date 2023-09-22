from django.contrib import admin
from apps.tracker.models import FoodAdvice
#from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(FoodAdvice)
#class adviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#    ...
#admin.site.register(FoodAdvice, adviceAdmin)

