from django.http import HttpResponse
from django.shortcuts import render, redirect
#from .models import Task


# Create your views here.
def home(request):
    return render(request, 'home.html')


def new(request):
    return render(request, 'new.html')


def form(request):
    # # task = Task.objects.all()
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     dob = request.POST.get('dob')
    #     age = request.POST.get('age')
    #     gender = request.POST.get('gender')
    #     phone = request.POST.get('phone')
    #     # email = request.POST.get('email')
    #     address = request.POST.get('address')
    #     task1 = Task(name=name,dob=dob,age=age,gender=gender,phone=phone,address=address)
    #     task1.save()

    return render(request, 'form.html')


def message(request):
    return render(request, 'message.html')
