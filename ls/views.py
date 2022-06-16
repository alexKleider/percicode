#!/usr/bin/env python3

# File: ls.views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Each view takes an HttpRequest parameter 
# and must return an HttpResponse object.

def home_page(request):
#1  return HttpResponse()
    return HttpResponse("<html><title>To-Do lists</title></html>")

