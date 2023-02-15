from django.contrib import admin
from .models import Object, ControlChart, RiskAnalysis


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


admin.site.register(Object, ObjectAdmin)
admin.site.register(ControlChart, ControlChartAdmin)
admin.site.register(RiskAnalysis, RiskAnalysisAdmin)
