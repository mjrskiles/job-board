from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'workorder_list.html', {})

def workorder_mockup(request):
    return render(request, 'workorder_list_mockup.html', {})
