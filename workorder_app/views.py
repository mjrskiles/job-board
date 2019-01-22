from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import WorkOrder

def index(request):
    workorders = WorkOrder.objects.order_by('-due_date')
    context = {'workorders': workorders}
    return render(request, 'workorder_list.html', context)

def workorder_mockup(request):
    return render(request, 'workorder_list_mockup.html', {})
