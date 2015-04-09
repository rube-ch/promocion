from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from prospectos.models import ProspectoForm, Prospecto, ProspectoBuapForm
from eventos.models import Evento
from django.db.models import Count
import pandas as pd
from django.contrib import messages
import numpy as np


# Create your views here.
@login_required
def prospecto_nuevo(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    messages.set_level(request, messages.SUCCESS)
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProspectoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, 'El Prospecto fue guardado correctamente.')
            # redirect to a new URL:
            return HttpResponseRedirect('/prospectos/nuevo/')
        messages.warning(request, 'Verifica los datos faltantes o con error.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProspectoForm()

    return render(request, 'prospectos/nuevo.html', {'form': form})

@login_required
def prospecto_buap(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
# if this is a POST request we need to process the form data
    messages.set_level(request, messages.SUCCESS)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProspectoBuapForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post = form.save(commit=False)
            evento, _ = Evento.objects.get_or_create(evento=162)
            post.evento = evento
            post.autor = request.user
            post.save()
            messages.success(request, 'El Prospecto BUAP fue guardado correctamente.')
            # redirect to a new URL:
            return HttpResponseRedirect('/prospectos/nuevobuap/')
        messages.warning(request, 'Verifica los datos faltantes o con error.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProspectoBuapForm()

    return render(request, 'prospectos/buap.html', {'form': form})

@login_required
def captura(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    values = User.objects.annotate(capturados=Count('prospecto'))
    return render(request, 'prospectos/captura.html', {'valores': values})

@login_required
def captura_evento(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    """
    Prospectos por evento, sin detalle de carreras.
    values = Evento.objects.annotate(capturados=Count('prospecto'))
    """
    qs = Prospecto.objects.all()
    q = qs.values('evento__nombre_evento', 'carrera')
    prospectos_df = pd.DataFrame.from_records(q)
    prospectos_df.rename(columns={'evento__nombre_evento': 'Evento', 'carrera': 'Carrera'}, inplace=True)

    values= prospectos_df.pivot_table(rows='Evento', cols='Carrera', aggfunc=len, margins=True,
                                      fill_value=0)

    return render(request, 'prospectos/captura_evento.html', {'valores': values.to_html(classes='table')})

@login_required
def captura_examen(request):

    """If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    values = User.objects.filter(prospecto__evento=162).annotate(capturados=Count('prospecto'))

    return render(request, 'prospectos/captura_examen.html', {'valores': values})

@login_required
def captura_buapsep(request):

    """If users are authenticated, direct them to the main page. Otherwise, take
     them to the login page.
    """

    qs = Prospecto.objects.all()
    q = qs.values('evento__nombre_evento', 'carrera', 'examen_buap')
    prospectos_df = pd.DataFrame.from_records(q)
    prospectos_df.rename(columns={'evento__nombre_evento': 'Evento', 'examen_buap': 'Examen'}, inplace=True)
    prospectos_df["Examen"].replace(to_replace=True, value="BUAP", inplace=True)
    prospectos_df["Examen"].replace(to_replace=False, value="SEP", inplace=True)
    prospectos_df["Examen"].fillna("SinInfo", inplace=True)
    # values = prospectos_df
    values= prospectos_df.pivot_table(rows='Evento', cols=['Examen', 'carrera'], aggfunc=len,
                                       margins=True)
    values.fillna(0, inplace=True)

    return render(request, 'prospectos/captura_buapsep.html', {'valores': values.to_html(classes='table')})
