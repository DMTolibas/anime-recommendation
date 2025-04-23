from django.contrib import admin
from .models import Anime, AnimeImport

from import_export.admin import ImportExportModelAdmin
from .resources import AnimeImportResource

#Import the necessary func for deleting records
from django.contrib import admin
from anime_list.models import AnimeImport

# Register your models here.
admin.site.register(Anime)

@admin.register(AnimeImport)
class AnimeImportAdmin(ImportExportModelAdmin):  #add the import and import functionality instead of other the standard django func
    resource_class = AnimeImportResource



""" 
#Make a button that delete all imported files using admin IU
@admin.action(description="Delete all imported records")
def delete_all(modeladmin, request, queryset):
    AnimeImport.objects.all().delete()

class AnimeImportAdmin(admin.ModelAdmin):
    actions = [delete_all] """

#Delete all files when there is a limit
""" from anime_list.models import AnimeImport

BATCH_SIZE = 500

while True:
    ids = list(AnimeImport.objects.values_list('id', flat=True)[:BATCH_SIZE])
    if not ids:
        break
    AnimeImport.objects.filter(id__in=ids).delete() """

