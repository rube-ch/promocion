__author__ = 'cin'

from django.conf.urls import *
from prospectos.views import *

urlpatterns = patterns('',

    # Main crm entrance.
    (r'^nuevo/$', prospecto_nuevo),
    (r'^nuevobuap/$', prospecto_buap),
    (r'^captura/$', captura),
    (r'^captura_evento/$', captura_evento),
    (r'^captura_examen/$', captura_examen),
    (r'^captura_buapsep/$', captura_buapsep),

)
