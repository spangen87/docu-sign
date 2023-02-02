from django.urls import path
from . import views

urlpatterns = [
    path('', views.forms, name='forms'),
    path('kontrollschema/', views.kontrollschema, name='kontrollschema'),
    path('objekt/', views.object, name='object'),
    path('nytt_objekt/', views.new_object, name='new_object'),
]
