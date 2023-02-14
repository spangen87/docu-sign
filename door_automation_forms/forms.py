from django import forms
from django.forms import ChoiceField, MultipleChoiceField
from .models import Object, ControlChart, RiskAnalysis, Choice


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


class RiskAnalysisForm(forms.ModelForm):
    """
    Form for handling risk analyser
    """

    SAFETY_CHOICES = [
        ('protective_covers', 'Skyddskåpor eller dylikt'),
        ('barriers', 'Barriärer'),
        ('obstacles', 'Hinder'),
        ('safety_sensors', 'Säkerhetssensorer'),
        ('low_energy_level', 'Low Energy-nivå'),
    ]

    A = forms.MultipleChoiceField(choices=SAFETY_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    B = forms.MultipleChoiceField(choices=SAFETY_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    C = forms.MultipleChoiceField(choices=SAFETY_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    D = forms.MultipleChoiceField(choices=SAFETY_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    E = forms.MultipleChoiceField(choices=SAFETY_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = RiskAnalysis
        fields = '__all__'
