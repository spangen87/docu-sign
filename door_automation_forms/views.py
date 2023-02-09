from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Object, ControlChart
from .forms import ObjectForm, ControlChartForm


def forms(request):
    """
    A view to return the forms page
    """
    return render(request, 'door_automation_forms/all_forms.html')


def control_charts(request):
    """
    A view to render all control charts
    """
    control_charts = ControlChart.objects.all()
    context = {
        'control_charts': control_charts,
    }

    return render(request, 'door_automation_forms/kontrollscheman.html', context)


def new_control_chart(request):
    """
    A view to return the kontrollschema form
    """
    if request.method == 'POST':
        form = ControlChartForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kontrollschema sparat!')
            return redirect('control_charts')
        else:
            messages.error(request, form.errors)
    else:
        form = ControlChartForm()

    context = {
        'form': form,
    }

    return render(request, 'door_automation_forms/nytt_kontrollschema.html', context)


def control_chart_details(request, control_chart_id):
    """
    View to render details for a control chart
    """
    control_chart = get_object_or_404(ControlChart, pk=control_chart_id)
    context = {
        'control_chart': control_chart,
    }
    template = 'door_automation_forms/kontrollschema_detaljer.html'

    return render(request, template, context)


def edit_control_chart(request, control_chart_id):
    """
    Edit a existing control chart
    """
    control_chart = get_object_or_404(ControlChart, pk=control_chart_id)
    if request.method == 'POST':
        form = ControlChartForm(
            request.POST, request.FILES, instance=control_chart)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uppdateringar sparade!')
            return redirect('control_charts')
        else:
            messages.error(request, form.errors)
    else:
        form = ControlChartForm(instance=control_chart)
    template = 'door_automation_forms/redigera_kontrollschema.html'
    context = {
        'form': form,
        'control_chart': control_chart,
    }

    return render(request, template, context)


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
