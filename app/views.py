from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def home(request):
	if request.user.is_authenticated():
		tasks = Task.objects.all().order_by('-created_date')
		return render(request, "home.html", {'tasks':tasks})
	else:
		return render(request, "intro.html", {})

def done(request):
	if request.user.is_authenticated():
		tasks = Task.objects.all().filter(done=True).order_by('-created_date')
		return render(request, "done.html", {'tasks':tasks})
	else:
		return render(request, "intro.html", {})

@api_view(['POST', ])
def login(request):
	if request.method == 'POST':
		username = request.data['key']
		password = request.data['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			username = auth.get_user(request).username
			print ('logged in succesfully')
			data = {
			'action': 'relocate',
			 }
		else:
			data = {
			'action': 'signup',

			  }
	else:
		 error = "Fuck"
		 return error
		 return Response(request.data)
	return Response(data)


@api_view(['POST', ])
def mark_done(request):
	task_id = request.data['task_id']
	task = Task.objects.get(id=task_id)
	task.done = True
	task.done_by = request.user.userprofile
	task.save()
	return Response(request.data)


@api_view(['POST', ])
def mark_undone(request):
	task_id = request.data['task_id']
	task = Task.objects.get(id=task_id)
	task.done = False
	task.save()
	return Response(request.data)

@api_view(['POST', ])
def delete(request):
	task_id = request.data['task_id']
	task = Task.objects.get(id=task_id)
	task.delete()
	return Response(request.data)

@api_view(['POST', ])
def edit(request):
	task_id = request.data['task_id']
	new_text = request.data['new_text']
	new_title = request.data['new_title']
	task = Task.objects.get(id=task_id)
	task.title = new_title
	task.text = new_text
	task.save()
	return Response(request.data)

   

@api_view(['POST', ])
def sign_up(request):
	if request.method == 'POST':
		username = request.data['key']
		password = request.data['password']
		check = User.objects.filter(username=username).exists()
		if check == True:
			print ('check')
			data = {
			'action': 'error',
			 }
		else:
			user = User.objects.create_user(username=username, password=password)
			userprofile = UserProfile.objects.create(user=user)
			user = auth.authenticate(username=username, password=password)
			auth.login(request, user)
			print (userprofile)
			data = {
			'action': 'relocate',

			  }
	else:
		 error = "Fuck"
		 return error
	return Response(data)


def add(request):
	title = request.POST.get('title')
	text =  request.POST.get('text')
	Task.objects.create(created_by=request.user.userprofile,text=text,title=title)
	return redirect('home')

@api_view(['POST', ])
def logout(request):
    auth.logout(request)
    return Response(request.data)
