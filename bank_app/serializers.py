from rest_framework import serializers
from .models import *


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name','email_address','cell_phone']