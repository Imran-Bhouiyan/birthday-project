from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 

class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__' 

