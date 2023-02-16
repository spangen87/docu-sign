from django import forms
from django.forms import ChoiceField, MultipleChoiceField
from .models import Object, ControlChart, RiskAnalysis


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

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ControlChart
        fields = '__all__'


class RiskAnalysisForm(forms.ModelForm):
    """
    Form for handling risk analyser
    """
    SAFETY_CHOICES = (
        ('protective_covers', 'Skyddskåpor eller dylikt'),
        ('barriers', 'Barriärer'),
        ('obstacles', 'Hinder'),
        ('safety_sensors', 'Säkerhetssensorer'),
        ('low_energy_level', 'Low Energy-nivå'),
    )

    A = forms.MultipleChoiceField(
        choices=SAFETY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="A. Klämrisk*",
        help_text="""*Område A och B ska skyddas med säkerhetssensorer. Övriga
        punkter säkras speciellt vid behov/säkerhetsrisk""")
    B = forms.MultipleChoiceField(
        choices=SAFETY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="B. Klämrisk*",
        help_text="""*Område A och B ska skyddas med säkerhetssensorer. Övriga
        punkter säkras speciellt vid behov/säkerhetsrisk""")
    C = forms.MultipleChoiceField(
        choices=SAFETY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="C. Klämrisk")
    D = forms.MultipleChoiceField(
        choices=SAFETY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="D. Klämrisk")
    E = forms.MultipleChoiceField(
        choices=SAFETY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="E. Klämrisk")

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = RiskAnalysis
        fields = '__all__'
