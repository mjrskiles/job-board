from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import date

from .models import WorkOrder

def index(request):
    workorders = WorkOrder.objects.order_by('due_date')

    today = date.today()
    for i in range(len(workorders)):
        # Add an index to number the table entries
        workorders[i].index = i + 1
        # Calculate if workorder should be highlighted as urgent
        days_until_due_date = (workorders[i].due_date - today).days
        if days_until_due_date < 30:
            workorders[i].is_urgent = True
        else:
            workorders[i].is_urgent = False

    context = {
        'workorders' : workorders
    }
    return render(request, 'workorder_list.html', context)

def workorder_mockup(request):
    return render(request, 'workorder_list_mockup.html', {})
