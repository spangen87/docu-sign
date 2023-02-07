from django import forms
from .models import Object, ControlChart


class ObjectForm(forms.ModelForm):

    class Meta:
        model = Object
        fields = [
            'name',
            'address',
            'constructor',
            'contact_person',
            'notes',
            'drawing',
        ]


class ControlChartForm(forms.ModelForm):

    class Meta:
        model = ControlChart
        fields = '__all__'
