__author__ = 'cin'

from django.conf.urls import *
from prospectos.views import *

urlpatterns = patterns('',

    # Main crm entrance.
    (r'^nuevo/', prospecto_nuevo),

)
