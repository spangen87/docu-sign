from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Object
from .forms import ObjectForm


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


def object(request):
    """
    A view to return the objects
    """
    objects = Object.objects.all()
    context = {
        'objects': objects,
    }

    return render(request, 'door_automation_forms/objekt.html', context)


def new_object(request):
    """
    Add new object
    """
    if request.method == 'POST':
        form = ObjectForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Nytt objekt tillagt!')
        else:
            messages.error(request, 'Något gick fel. Kolla så att formuläret är korrekt ifyllt.')
    else:
        form = ObjectForm()

    template = 'door_automation_forms/nytt_objekt.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
