from django.http import HttpResponse
from django.shortcuts import render


def about(res):
    return HttpResponse('<h1>This is the about page</h1>')

def users(res):
    return render(res, 'users.html')
