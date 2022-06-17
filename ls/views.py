#!/usr/bin/env python3

# File: ls.views.py

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Each view takes an HttpRequest parameter 
# and must return an HttpResponse object.
# ...but we bypass that by using templates & 'render' functionality
# simply pasing the request to django.shortcuts.render:

def home_page(request):
    """
    pass variables from our view code => HTML templates
    """
#1  return HttpResponse()
#2  return HttpResponse("<html><title>To-Do lists</title></html>")
#   if request.method == 'POST':
#       return HttpResponse(request.POST['item_text'])
#   return render(request, 'home.html')
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
        })
    
