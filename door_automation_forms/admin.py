from django.contrib import admin
from .models import Object


class ObjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'constructor',
        'contact_person',
    )

    ordering = ('name',)


admin.site.register(Object, ObjectAdmin)
