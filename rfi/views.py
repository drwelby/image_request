from rfi.models import RequestForImagery, RequestForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

def request_info(request, pk):
    try:
        rfi = RequestForImagery.objects.get(pk=int(pk))
    except RequestForImagery.DoesNotExist:
        return render_to_response('rfi/missing.html')
    return render_to_response('rfi/info_request.html', {'rfi': rfi})

def new_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rfi/complete/')

    else:
        form = RequestForm()

    return render(request, 'rfi/new.html', {'form': form})

def complete(request):
    return render_to_response('rfi/complete.html')
