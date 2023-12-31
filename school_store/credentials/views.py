from django.contrib import auth, messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['c_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password are not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/new')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
