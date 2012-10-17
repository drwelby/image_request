from rfi.models import RequestForImagery, RequestForm
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def request_info(request, pk):
    try:
        rfi = RequestForImagery.objects.get(pk=int(pk))
    except RequestForImagery.DoesNotExist:
        return render_to_response('rfi/missing.html')
    return render_to_response('rfi/info_request.html', {'rfi': rfi})

def info_window(request, pk):
    if request.method.upper() == 'OPTIONS':
        r = HttpResponse()
        r['Access-Control-Allow-Origin'] = '*'
        r['Access-Control-Allow-Headers'] = 'Authorization, X-Requested-With'
        r['Access-Control-Allow-Methods'] = 'GET,OPTIONS'
        r['Access-Control-Allow-Credentials'] = 'true'
        return r

    rfi = get_object_or_404(RequestForImagery, pk=int(pk))
    r = render_to_response('rfi/info_window.html', {'rfi': rfi})
    # cross-domain headers
    r['Access-Control-Allow-Origin'] = '*'
    r['Access-Control-Allow-Headers'] = 'Authorization'
    return r

def edit_request(request, pk):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rfi/complete/')

    else:
        rfi = get_object_or_404(RequestForImagery, pk=int(pk))
        form = RequestForm(instance=rfi)

    return render(request, 'rfi/new.html', {'form': form})

def new_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rfi/complete/')

    else:
        form = RequestForm(initial = request.GET)

    return render(request, 'rfi/new.html', {'form': form})

def complete(request):
    return render_to_response('rfi/complete.html')
