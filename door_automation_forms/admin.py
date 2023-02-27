from django.contrib import admin
from .models import Object, ControlChart, RiskAnalysis, InstallationDescription, Service


class ObjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'constructor',
        'contact_person',
    )

    ordering = ('name',)


class ControlChartAdmin(admin.ModelAdmin):
    list_display = (
        'object',
        'position_id',
        'date',
        'done_by',
    )

    ordering = ('date', 'object')


class RiskAnalysisAdmin(admin.ModelAdmin):
    list_display = (
        'object',
        'door_id',
        'date',
        'done_by',
    )

    ordering = ('date', 'object')


class InstallationDescriptionAdmin(admin.ModelAdmin):
    list_display = (
        'object_name',
        'door_name',
        'date_in_use',
        'technician',
    )

    ordering = ('object_name', 'door_name')


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'door_automatic',
        'service_year',
        'date',
        'technician',
    )


admin.site.register(Object, ObjectAdmin)
admin.site.register(ControlChart, ControlChartAdmin)
admin.site.register(RiskAnalysis, RiskAnalysisAdmin)
admin.site.register(InstallationDescription, InstallationDescriptionAdmin)
admin.site.register(Service, ServiceAdmin)
