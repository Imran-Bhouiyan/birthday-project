from django.urls import path 

from .views import * 

urlpatterns = [
    path('customers/' , CustomerView.as_view()),
    path('customer/<int:pk>/' , CustomerView.as_view()),
    path('reports/' , ReportView.as_view()),

]
