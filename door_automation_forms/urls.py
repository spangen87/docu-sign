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
    path('hello/pdf/', views.PDFView.as_view(), name='hello_pdf'),
]
