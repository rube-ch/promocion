__author__ = 'cin'

from django.conf.urls import *
from crm.views import *

urlpatterns = patterns('',

    # Main crm entrance.
    (r'^$', crm_main_page),

)