from django.urls import path
from . import views

urlpatterns = [
    path('', views.forms, name='forms'),
    path('kontrollschema/', views.kontrollschema, name='kontrollschema'),
    path('objekt/', views.object, name='object'),
    path('nytt_objekt/', views.new_object, name='new_object'),
    path('objekt_detaljer/<int:object_id>', views.object_details, name='object_details'),
    path('redigera_objekt/<int:object_id>', views.edit_object, name='edit_object'),
]
