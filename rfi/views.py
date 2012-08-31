from rfi.models import RequestForImagery
from django.shortcuts import render_to_response

def request_info(request, pk):
    try:
        rfi = RequestForImagery.objects.get(pk=int(pk))
    except RequestForImagery.DoesNotExist:
        return render_to_response('rfi/missing.html')
    return render_to_response('rfi/info_request.html', {'rfi': rfi})
