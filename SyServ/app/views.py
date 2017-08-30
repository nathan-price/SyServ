"""
Definition of views.
"""

import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import gsi

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

@csrf_exempt
def gsiupdate(request):
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        #print(request.POST)
        #return JsonResponse({'status':'Success', 'msg':'POST'})
        try:
            obj = gsi.objects.get(matchid=data['matchid'], steamid=data['steamid'])
            obj.hp = data['hp']
            obj.mana = data['mana']
            obj.gpm = data['gpm']
            obj.xpm = data['xpm']
            obj.alive = data['alive']
            obj.save()
            qs = gsi.objects.filter(matchid=data['matchid'], team=data['team'])
            return JsonResponse(serializers.serialize('json', qs), safe=False)
        except:
            return JsonResponse({'status':'Fail', 'msg':'POST'})
    elif request.method=='GET':
        return JsonResponse({'status':'Success', 'msg':'GET'})
    else:
        return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})