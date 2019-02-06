from django.contrib import admin
from .models import WorkOrder
from .models import AppConfig

# Register your models here.
admin.site.register(WorkOrder)
admin.site.register(AppConfig)