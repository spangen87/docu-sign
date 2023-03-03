from django import forms
from django.forms import ChoiceField, MultipleChoiceField
from .models import Object, ControlChart, RiskAnalysis, InstallationDescription, Service


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

    # def __init__(self, *args, **kwargs):
    #     super(ControlChartForm, self).__init__(*args, **kwargs)
    #     if self.instance.object:
    #         self.fields['position_id'].queryset = RiskAnalysis.objects.filter(object__exact=self.instance.object)


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
        ('note', 'Anmärkning'),
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

    A_note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        label='Anmärkningar',
        label_suffix=': ',
    )
    B_note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        label='Anmärkningar',
        label_suffix=': ',
    )
    C_note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        label='Anmärkningar',
        label_suffix=': ',
    )
    D_note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        label='Anmärkningar',
        label_suffix=': ',
    )
    E_note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        label='Anmärkningar',
        label_suffix=': ',
    )

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = RiskAnalysis
        fields = '__all__'


class InstallationDescriptionForm(forms.ModelForm):
    date_in_use = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    object_name = forms.ModelChoiceField(
        queryset=Object.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_object_name', 'onchange': 'filter_doors()'}),
        label='Välj objekt'
    )
    door_name = forms.ModelChoiceField(
        queryset=RiskAnalysis.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_door_name'}),
        label='Välj dörr'
    )

    class Meta:
        model = InstallationDescription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'object_name' in self.data:
            try:
                object_id = int(self.data.get('object_name'))
                self.fields['door_name'].queryset = RiskAnalysis.objects.filter(object_name_id=object_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty RiskAnalysis queryset
        elif self.instance.pk:
            self.fields['door_name'].queryset = self.instance.object_name.riskanalysis_set.order_by('door_name')



class ServiceForm(forms.ModelForm):

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Service
        fields = '__all__'
