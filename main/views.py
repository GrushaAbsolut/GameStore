from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Products


def home(request):
    return render(request, 'main/home.html')


def novosti(request):
    return render(request, 'main/novosti.html')


def tovar(request):
    product = Products.objects.all()
    return render(request, 'main/tovar.html', {'product': product})


def contact(request):
    return render(request, 'main/contact.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/admin/')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'main/login.html')


