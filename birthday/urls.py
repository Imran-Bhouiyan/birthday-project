from django.urls import path 

from .views import * 

urlpatterns = [
    path('customers/' , CustomerView()),
    path('customer/<int:pk>/' , CustomerView()),
    path('reports/' , ReportView()),

]
