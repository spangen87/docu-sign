from django.urls import path
from . import views

urlpatterns = [
    path('', views.forms, name='forms'),
    path('nytt_kontrollschema/', views.new_control_chart, name='new_control_chart'),
    path('kontrollscheman/', views.control_charts, name='control_charts'),
    path('kontrollschema_detaljer/<int:control_chart_id>', views.control_chart_details, name='control_chart_details'),
    path('redigera_kontrollschema/<int:control_chart_id>', views.edit_control_chart, name='edit_control_chart'),
    path('objekt/', views.object, name='object'),
    path('nytt_objekt/', views.new_object, name='new_object'),
    path('objekt_detaljer/<int:object_id>', views.object_details, name='object_details'),
    path('redigera_objekt/<int:object_id>', views.edit_object, name='edit_object'),
    path('ny_riskanalys/', views.new_risk_analysis, name='new_risk_analysis'),
    path('riskanalyser/', views.risk_analysis, name='risk_analysis'),
    path('redigera_riskanalys/<int:risk_analysis_id>', views.edit_risk_analysis, name='edit_risk_analysis'),
    path('riskanalys_detaljer/<int:risk_analysis_id>', views.risk_analysis_details, name='risk_analysis_details'),
    path('generate_pdf/<int:control_chart_id>', views.generate_pdf, name='generate_pdf'),
    path('print_riskanalys/<int:risk_analysis_id>', views.risk_analysis_pdf, name='risk_analysis_pdf'),
    path('print_installationsbeskrivning/<int:installation_description_id>', views.installation_description_pdf, name='installation_description_pdf'),
    path('ny_installationsbeskrivning/', views.new_installation_description, name='new_installation_description'),
    path('installationsbeskrivning/', views.installation_description, name='installation_description'),
    path('installationsbeskrivning_detaljer/<int:installation_description_id>', views.installation_description_details, name='installation_description_details'),
    path('redigera_installationsbeskrivning/<int:installation_description_id>', views.edit_installation_description, name='edit_installation_description'),
]
