from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
#from rest_framework import viewsets
#from faculty_request.serializers import faculty_Serializer,admin_Serializer,labtech_Serializer
from faculty_request.models import Requests
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods 

'''class faculty_view(viewsets.ModelViewSet):
	queryset=request.objects.all()
	serializer_class=faculty_Serializer



class admin_view(viewsets.ModelViewSet):
i        queryset=request.objects.all()
        serializer_class=admin_Serializer




class labtech_view(viewsets.ModelViewSet):
        queryset=request.objects.all()
        serializer_class=labtech_Serializer;'''

@csrf_exempt
@require_http_methods(['POST'])
def request_save(request):
    post = request.POST
    requests = Requests(
            faculty_Name = User.objects.get(id=post["faculty_Name"]),
            labtech_Name = User.objects.get(id=post['labtech_Name']),
            uploaded=post['upload'],
            subject = post['subject'],
            description = post['description'],
            due_date = post['due_date'],
            request_Type = post['request_Type'],
            request_status = 'Pending',
    )
    try:
        requests.save()
        data = {'data': 'Request Created'}
        code = 201
    except:
        data = {'message': 'Request not saved'}
        code = 400
    return HttpResponse(simplejson.dumps(data), status=code)


def admin_view(request):
	faculty= Requests.objects.all()
	data = serializers.serialize('json', faculty)
	return HttpResponse(data, mimetype = 'application/json')

#def user_view(request):
#   post = request.POST
#   requests = models.Requests(
#	#faculty_Name = User.objects.get(id=post['faculty_Name']),
#	labtech_Name = User.objects.get(id=request.User.id),
#	#subject=post['subject'],
#	#description=post['description'],
#	#due_date=post['due_date'],
#	#request_Type=post['request_Type'],
#	#request_status=post['request_status'],
#) 
#   data=serializers.serialize('json',requests)
#   return HttpResponse (data,mimetype = 'aplication/json')  

def user_view(request, user=None):
	if not user:
		user = request.user
	else:
		user = User.objects.get(pk=user)
	requests = Requests.objects.filter(labtech_Name=user)
	requests = [x.to_dict() for x in requests]
	data = {'message': '', 'requests': requests} #simplejson.dumps(requests, indent=2)}
	data = simplejson.dumps(data, indent=2)
	return HttpResponse(data, status=200, mimetype='application/json')
	

@csrf_exempt
@require_http_methods(['POST'])
def request_update(request):
	post = request.POST
	requests= Requests.objects.get(id=post['id'])
	requests.labtech_Name=User.objects.get(id=post["labtech_Name"])
	requests.request_status=post['request_status']


	try:
		requests.save()
		data={'data': 'Request Updated'}
		code=200

	except:
		data={'message':'request not updated'}
		code=400
	return HttpResponse(simplejson.dumps(data), status=code)
