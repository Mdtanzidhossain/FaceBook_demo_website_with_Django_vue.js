from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Story
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import time

@login_required
def home(request):
	context = { 
		'posts': Story.objects.all().order_by('-date')
	}
	return render(request, 'facebook2/index.html', context)

def profile(request):
	# id = request.user.email
	return render(request, 'facebook2/profile.html')

def signin(request):
	if (request.method == 'GET'):
		return render(request, 'facebook2/signin.html')
	elif (request.method == 'POST'):
		u = request.POST.get('user', '')
		p = request.POST.get('pass', '')
		user = authenticate(username=u, password=p)
		if user is None:
			messages.error(request, 'Invalid username or password')
			# messages.info(request, 'extra info')
			return render(request, 'facebook2/signin.html')
		else:
			login(request, user)
			return redirect('home-page')

def signout(request):
	logout(request)
	return redirect('signin')

@login_required
def createpost(request):
	c = request.POST.get('content', '')
	t = request.POST.get('tags', '')
	u = request.user
	s1 = Story(content=c, tag=t, author=u)
	s1.save()
	messages.info(request, 'Post created successfully!')
	return redirect('home-page')

@login_required
def editpost(request, id):
	s1 = Story.objects.get(id=id)

	if (request.user != s1.author):
		return redirect('home-page')

	if (request.method == 'GET'):
		return render(request, 'facebook2/editpost.html', {'old_post': s1})
	elif (request.method == 'POST'):
		s1.content = request.POST.get('content', '')
		s1.tag = request.POST.get('tags', '')
		s1.date = timezone.now()
		s1.save()
		messages.info(request, "Post updated!")
		return redirect('home-page')


@login_required
def deletepost(request, id):
	s1 = Story.objects.get(id=id)

	if (request.user != s1.author):
		return redirect('home-page')

	if (request.method == 'GET'):
		return render(request, 'facebook2/deletepost.html', {'old_post': s1})
	elif (request.method == 'POST'):
		s1.delete()
		messages.info(request, "Post deleted!")
		return redirect('home-page')

def stories(request):
	# time.sleep(5)
	data = list(Story.objects.all().order_by('-date').values())
	return JsonResponse(data, safe=False)


def vuetest(request):
	return render(request, 'facebook2/vuetest.html')

def vuehomepage(request):
	return render(request, 'facebook2/vuehomepage.html')