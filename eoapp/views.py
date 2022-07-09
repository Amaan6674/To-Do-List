from django.shortcuts import render,redirect
from .models import TaskModel

def home(request):
	if request.user.is_authenticated:
		return render(request,'home.html')
	else:
		return redirect('ulogin')

def create(request):
	if request.method=="POST":
		t=request.POST.get("task")
		ta=TaskModel.objects.create(task=t,us=request.user)
		ta.save()
		return render(request,'create.html',{'msg':'Task Added To Your List'})
	else:
		return render(request,'create.html')


def viewtask(request):
	if request.user.is_authenticated:
		d=TaskModel.objects.filter(us=request.user)
		return render(request,'viewtask.html',{'data':d})
	else:
		return redirect('ulogin')


def deletetask(request,t):
	ds=TaskModel.objects.get(task=t)
	ds.delete()
	return redirect('viewtask')