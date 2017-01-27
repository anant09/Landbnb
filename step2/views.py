from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Courier
from models import User
import json
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
# Create your views here.

    
    
    
def req_made(request):
    context_dict={'boldmessage': Courier.objects.all() }
    return render(request,'step2/request_made.html',context=context_dict)
    
    
def about(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # form = NameForm(request.POST)
        # check whether it's valid:
        print "post variables", request.POST
        print "entered post"
        # if form.is_valid():
        q= Courier(user=request.user, weight=request.POST['weight'],height=request.POST['height'],width=request.POST['width'],length=request.POST['length'],location_from=request.POST['location_from'],location_to=request.POST['location_to'])
        q.save()
        return HttpResponseRedirect('/step2/request_made/')
        # else:
            # print "errors",form.errors
            
    # if a GET (or any other method) we'll create a blank form
    else:
        # form = NameForm()
        user = request.user

    return render(request, 'step2/welcome.html', {'user':request.user})

@login_required
def view_courier(request, loc_from,loc_to):
    
    courier_dict={'Courier': Courier.objects.filter(location_to = loc_to,location_from=loc_from) }
    # response_data = Courier.objects.get(location_to = loc_to,location_from=loc_from)
    for key,value in courier_dict.iteritems() :
        print key,value
    print "now json"
    response = JsonResponse(courier_dict, safe=False)
    print response
    return HttpResponseRedirect('/home/')