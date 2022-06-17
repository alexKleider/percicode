#!/usr/bin/env python3

# File: ls.views.py

from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.
# Each view takes an HttpRequest parameter 
# and must return an HttpResponse object.
# ...but we bypass that by using templates & 'render' functionality
# simply pasing the request to django.shortcuts.render:

def home_page(request):
#1  return HttpResponse()
#2  return HttpResponse("<html><title>To-Do lists</title></html>")
    return render(request, 'home.html')
