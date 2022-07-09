from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from random import randrange
from todo_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def usignup(request):
	if request.method=="POST":
		un=request.POST.get("un")
		em=request.POST.get("em")
		try:
			usr=User.objects.get(username=un)
			return render(request,'usignup.html',{'msg':'username already taken'})
		except User.DoesNotExist:
			try:
				usr=User.objects.get(email=em)
				return render(request,'usignup.html',{'msg':'email already registered'})
			except User.DoesNotExist:
				text="1234567890abcdefghojglmnopqrstuvwxyz"
				pw=""
				for i in range(6):
					pw= pw + text[randrange(len(text))]
				
				send_mail("Welcome to Amaan's Django Website","Your Password Is "+ pw,EMAIL_HOST_USER,[em])
				usr=User.objects.create_user(username=un,password=pw,email=em)
				usr.save()
				return redirect('ulogin')
	else:
		return render(request,'usignup.html')

def ulogin(request):
	if request.method=="POST":
		un=request.POST.get('un')
		pw=request.POST.get("pw")
		usr=authenticate(username=un,password=pw)
		if usr is None:
			return render(request,'ulogin.html',{'msg':'Invalid Credentials'})
		else:
			login(request,usr)
			return redirect('home')
	else:
		return render(request,'ulogin.html')

def ulogout(request):
	logout(request)
	return redirect('ulogin')

def uresetpassword(request):
	if request.method=="POST":
		un=request.POST.get("un")
		em=request.POST.get("em")
		try:
			usr=User.objects.get(username=un) and User.objects.get(email=em)
			text="1234567890abcdefghojglmnopqrstuvwxyz"
			pw=""
			for i in range(6):
				pw= pw + text[randrange(len(text))]
			send_mail("Welcome to Amaan's Django Website","Your Password Is "+ pw,EMAIL_HOST_USER,[em])
			usr.set_password(pw)
			usr.save()
			return redirect('ulogin')
		except User.DoesNotExist:
			return render(request,'uresetpassword.html',{'msg':'Invalid Credentials'})

	else:
		return render(request,'uresetpassword.html')
