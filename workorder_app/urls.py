from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mockup/', views.workorder_mockup, name='mockup'),
]
