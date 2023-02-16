from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Object, ControlChart, RiskAnalysis
from .forms import ObjectForm, ControlChartForm, RiskAnalysisForm
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template, render_to_string
from django.db.models import Q
from django.db.models.functions import Lower
from weasyprint import HTML
import tempfile


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
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'object':
                sortkey = 'lower_object'
                control_charts = control_charts.annotate(lower_object=Lower('object'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            control_charts = control_charts.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Ingen sökterm angiven!")

            queries = Q(
                object__name__icontains=query) | Q(
                    position_id__door_id__icontains=query)
            control_charts = control_charts.filter(queries)

    template = 'door_automation_forms/kontrollscheman.html'

    current_sorting = f'{sort}_{direction}'

    context = {
        'control_charts': control_charts,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


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


def generate_pdf(request, control_chart_id):

    control_chart = get_object_or_404(ControlChart, pk=control_chart_id)

    # Return the PDF file as a response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=kontrollschema.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    # Render the HTML template to a string
    html_string = render_to_string('door_automation_forms/print.html', {'control_chart': control_chart})

    # Generate the PDF file
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response


def new_risk_analysis(request):
    """
    A view to return the riskanalys form
    """
    if request.method == 'POST':
        form = RiskAnalysisForm(request.POST)
        if form.is_valid():
            # Save the form
            form.save()
            messages.success(request, 'Riskanalys sparad!')
            return redirect('risk_analysis')
        else:
            messages.error(request, form.errors)
    else:
        form = RiskAnalysisForm()

    context = {
        'form': form,
    }

    template = 'door_automation_forms/ny_riskanalys.html'

    return render(request, template, context)


def risk_analysis(request):
    """
    A view to render all risk analysis
    """
    analysis = RiskAnalysis.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'object':
                sortkey = 'lower_object'
                analysis = analysis.annotate(lower_object=Lower('object'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            analysis = analysis.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Ingen sökterm angiven!")

            queries = Q(
                object__name__icontains=query) | Q(
                    door_id__icontains=query)
            analysis = analysis.filter(queries)

    template = 'door_automation_forms/riskanalyser.html'

    current_sorting = f'{sort}_{direction}'

    context = {
        'analysis': analysis,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def risk_analysis_details(request, risk_analysis_id):
    """
    View details of a object
    """
    risk_analysis = get_object_or_404(RiskAnalysis, pk=risk_analysis_id)
    context = {
        'risk_analysis': risk_analysis,
    }
    template = 'door_automation_forms/riskanalys_detaljer.html'

    return render(request, template, context)


def edit_risk_analysis(request, risk_analysis_id):
    """
    Edit a existing risk analysis
    """
    risk_analysis = get_object_or_404(RiskAnalysis, pk=risk_analysis_id)
    if request.method == 'POST':
        form = RiskAnalysisForm(
            request.POST, request.FILES, instance=risk_analysis)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uppdateringar sparade!')
            return redirect('risk_analysis')
        else:
            messages.error(request, form.errors)
    else:
        form = RiskAnalysisForm(instance=risk_analysis)
    template = 'door_automation_forms/redigera_riskanalys.html'
    context = {
        'form': form,
        'risk_analysis': risk_analysis,
    }

    return render(request, template, context)


def risk_analysis_pdf(request, risk_analysis_id):

    risk_analysis = get_object_or_404(RiskAnalysis, pk=risk_analysis_id)

    # Return the PDF file as a response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=riskanalys.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    # Render the HTML template to a string
    html_string = render_to_string('door_automation_forms/print_risk_analysis.html', {'risk_analysis': risk_analysis, 'MEDIA_URL': settings.MEDIA_URL,})

    # Generate the PDF file
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response
