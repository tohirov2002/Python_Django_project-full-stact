from django.contrib import admin

# Register your models here.
from app_comanders.models import Commander

class CommandersAdmin(admin.ModelAdmin):
    list_display = ('id','name','year')

admin.site.register(Commander,CommandersAdmin)