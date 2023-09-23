from django.contrib import admin
from apps.tracker.models import FoodAdvice
# Library for importing and exporting data
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#admin.site.register(FoodAdvice)
#class adviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#    ...
#admin.site.register(FoodAdvice, adviceAdmin)

# Import/export data via admin panel
class adviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(FoodAdvice, adviceAdmin)
