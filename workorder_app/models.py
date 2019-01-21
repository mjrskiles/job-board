from django.db import models
import datetime

# Create your models here.

class WorkOrder(models.Model):
    def __str__(self):
        return self.workorder_number

    workorder_number = models.CharField(max_length=200)
    machine_size = models.IntegerField(default=0)
    machine_type = models.CharField(max_length=200)
    due_date = models.DateField(default=datetime.date.today)