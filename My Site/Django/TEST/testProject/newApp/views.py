from django.shortcuts import render

def home(req):
    return render(req, 'home.html')

def test(req):
    return render(req, 'test.html')

def demo(req):
    return render(req, 'demo.html')
