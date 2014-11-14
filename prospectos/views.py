from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from prospectos.models import ProspectoForm

# Create your views here.
@login_required
def prospecto_nuevo(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
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
            # redirect to a new URL:
            return HttpResponseRedirect('/prospectos/nuevo/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProspectoForm()

    return render(request, 'prospectos/nuevo.html', {'form': form})