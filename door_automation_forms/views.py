from django.shortcuts import render


def forms(request):
    """
    A view to return the forms page
    """
    return render(request, 'door_automation_forms/all_forms.html')


def kontrollschema(request):
    """
    A view to return the kontrollschema form
    """
    return render(request, 'door_automation_forms/kontrollschema.html')
