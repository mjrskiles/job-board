from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import date

from .models import WorkOrder
from .models import AppConfig

def index(request):
    workorders = WorkOrder.objects.order_by('due_date')
    config = get_app_config()

    today = date.today()
    for i in range(len(workorders)):
        # Add an index to number the table entries
        workorders[i].index = i + 1
        # Calculate if workorder should be highlighted as urgent
        days_until_due_date = (workorders[i].due_date - today).days
        if days_until_due_date < config['DAYS_URGENT_WITHIN']:
            workorders[i].is_urgent = True
        else:
            workorders[i].is_urgent = False

    paginator = Paginator(workorders, config['ROWS_PER_PAGE'])
    page = request.GET.get('page')
    if not page:
        page = '1'
    paginated_workorders = paginator.get_page(page)

    num_pages = paginator.num_pages

    context = {
        'workorders'       : paginated_workorders,
        'current_page_num' : page,
        'total_num_pages'  : num_pages,
        'next_page'        : get_next_page(page, num_pages),
        'refresh_rate'     : config['REFRESH_RATE'],
        'row_height'       : (str((100 / config['ROWS_PER_PAGE'])) + '%') or '25%',
        'debug'            : config['DEBUG']
    }

    if request.GET.get('ajax') == 'true':
        # return render_to_string('table.html', context, request)
        return render(request, 'table.html', context)

    else:
        return render(request, 'workorder_list.html', context)

def workorder_mockup(request):
    return render(request, 'workorder_list_mockup.html', {})

def get_next_page(current_page, total_pages):
    next_page = (int(current_page) % int(total_pages)) + 1
    return str(next_page)

def get_app_config():
    app_config_table = AppConfig.objects.all()
    if len(app_config_table):
        app_config = AppConfig.objects.get(id=1)
        config = {
            'ROWS_PER_PAGE' : app_config.rows_per_page,
            'DAYS_URGENT_WITHIN' : app_config.days_urgent_within,
            'REFRESH_RATE' : app_config.refresh_rate_seconds * 1000,
            'DEBUG' : app_config.debug
        }   
    else:
        config = {
            'ROWS_PER_PAGE' : 4,
            'DAYS_URGENT_WITHIN' : 30,
            'REFRESH_RATE' : 7000,
            'DEBUG' : False
        }
    return config
