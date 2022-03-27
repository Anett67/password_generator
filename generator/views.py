from django.shortcuts import render
from django.http import HttpResponse
import random 

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    charachters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        charachters.extend(list('!@?:/#&$%*^'))
    
    if request.GET.get('numbers'):
        charachters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    password = ''

    for x in range(length):
        password += random.choice(charachters)

    return render(request, 'generator/password.html', {
        'password': password
    })
