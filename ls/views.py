#!/usr/bin/env python3

# File: ls.views.py

# from django.http import HttpResponse
from django.shortcuts import redirect, render
from ls.models import Item

# Create your views here.
# Each view takes an HttpRequest parameter 
# and must return an HttpResponse object.
# ...but we bypass that by using templates & 'render' functionality
# simply pasing the request to django.shortcuts.render:

"""
A view function has two jobs:
1. process user input
2. return an appropriate response
"""

def home_page(request):
    """
    pass variables from our view code => HTML templates
    """
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')
    
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
