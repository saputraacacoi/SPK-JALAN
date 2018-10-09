from django.contrib import admin
from orm.models import Alternatif
# Register your models here.
class AlternatifAdmin(admin.ModelAdmin):
    pass
admin.site.register(Alternatif, AlternatifAdmin)