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

    def to_representation(self, instance):
        
        data_set = {

            'id': instance.id,
            "customer_id": instance.customer.id,
            "customer_name": instance.customer.full_name,
            "customer_email": instance.customer.email,
            "customer_birthdate": instance.customer.birthdate,
            "created_at": instance.created_at
        }
        return data_set