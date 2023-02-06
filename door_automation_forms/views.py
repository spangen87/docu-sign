from django.shortcuts import render, get_object_or_404, redirect
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
        form = ObjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nytt objekt tillagt!')
            return redirect('object')
        else:
            messages.error(request, form.errors)
    else:
        form = ObjectForm()

    template = 'door_automation_forms/nytt_objekt.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def object_details(request, object_id):
    """
    View details of a object
    """
    object = get_object_or_404(Object, pk=object_id)
    context = {
        'object': object,
    }
    template = 'door_automation_forms/objekt_detaljer.html'

    return render(request, template, context)


def edit_object(request, object_id):
    """
    Edit a existing object
    """
    object = get_object_or_404(Object, pk=object_id)
    if request.method == 'POST':
        form = ObjectForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uppdateringar sparade!')
            return redirect('object')
        else:
            messages.error(request, form.errors)
    else:
        form = ObjectForm(instance=object)
    template = 'door_automation_forms/redigera_objekt.html'
    context = {
        'form': form,
        'object': object,
    }

    return render(request, template, context)
