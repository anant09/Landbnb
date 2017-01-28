from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
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
        subject = 'Landbnb order'
        message = 'Your order has been recorded successfully. Please notify if any of the following details are incorrect or need to be changed:- \nWeight :'+ str(request.POST['weight'])+'\nHeight: '+str(request.POST['height'])+'\nWidth: '+str(request.POST['width'])+'\nLength: '+str(request.POST['length'])+'\nFrom: '+str(request.POST['location_from'])+'\nDestination: '+str(request.POST['location_to'])
        from_email = settings.EMAIL_HOST_USER
        to_list = [request.user.email]

        send_mail(subject,message,from_email,to_list,fail_silently = True)
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
    
    json_data = {}
    i = 0
    for items in Courier.objects.filter(location_to = loc_to,location_from=loc_from):
        json_data[i] = ''
        json_data[i] = json_data[i] + str(items.weight) + ':' + str(items.height) + ':' + str(items.width) + ':' + str(items.length) + ':' + items.location_to + ':' + items.location_from
        print json_data[i]
        i = i+1
    courier_dict={'Courier': Courier.objects.filter(location_to = loc_to,location_from=loc_from) }
    # response_data = Courier.objects.get(location_to = loc_to,location_from=loc_from)

    for key,value in json_data.iteritems():
        print json_data[key]
    print "now json"
    response = JsonResponse(json_data, safe=False)
    print response
    return HttpResponseRedirect('/home/')