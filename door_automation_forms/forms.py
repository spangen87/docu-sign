from django import forms
from .models import Object


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
