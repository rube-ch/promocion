from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def prospecto_nuevo(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render_to_response('prospectos/nuevo.html')