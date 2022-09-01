from django.shortcuts import render
from django.http import HttpResponse
import random


def home(req):
    return render(req, 'generator/home.html')


def password(req):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if req.GET.get('uppercase'):
        characters.extend((list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))
    if req.GET.get('numbers'):
        characters.extend((list('123456789')))
    if req.GET.get('specialcharacters'):
        characters.extend((list('@#$%^&*!()')))
    print(characters)
    generatedPassword = ''
    length = int(req.GET.get('length', 200))
    for i in range(length):
        index = random.randrange(len(characters))
        generatedPassword += characters[index]

    return render(req, 'generator/password.html', {'password': generatedPassword})
